// Porteiro do 148 Estúdio no Cloudflare: só entrega o site para quem sabe a senha.
// A senha fica no segredo SENHA do Worker (painel da Cloudflare), nunca no código.
// Sem o segredo, o site fica fechado para todo mundo.

const FECHADO = 'O 148 Estúdio está fechado. Defina o segredo SENHA no painel da Cloudflare: ' +
  'Workers & Pages > 148studio > Settings > Variables and Secrets > Add (tipo Secret).'

const texto = (corpo, status, extra = {}) =>
  new Response(corpo, { status, headers: { 'content-type': 'text/plain; charset=utf-8', 'cache-control': 'no-store', ...extra } })

const resumo = async valor => new Uint8Array(await crypto.subtle.digest('SHA-256', new TextEncoder().encode(valor)))

/** A senha digitada no pedido de login do navegador (o nome de usuário é ignorado). */
function senhaDoPedido(request) {
  const [tipo, valor] = (request.headers.get('Authorization') || '').split(' ')
  if (tipo !== 'Basic' || !valor) return null
  try {
    const decodificado = new TextDecoder().decode(Uint8Array.from(atob(valor), ch => ch.charCodeAt(0)))
    return decodificado.slice(decodificado.indexOf(':') + 1)
  } catch {
    return null
  }
}

export default {
  async fetch(request, env) {
    if (!env.SENHA) return texto(FECHADO, 503)
    const senha = senhaDoPedido(request)
    if (senha !== null) {
      const [a, b] = await Promise.all([resumo(senha), resumo(env.SENHA)])
      if (crypto.subtle.timingSafeEqual(a, b)) {
        const resposta = await env.ASSETS.fetch(request)
        const protegida = new Response(resposta.body, resposta)
        protegida.headers.set('cache-control', 'private, no-store')
        protegida.headers.set('x-robots-tag', 'noindex, nofollow')
        return protegida
      }
    }
    return texto('Acesso restrito ao 148 Estúdio.', 401, { 'www-authenticate': 'Basic realm="148 Estudio", charset="UTF-8"' })
  },
}
