# Statikus / AI-builder funkciók

A `ux-terv.md` 5. szekciójához. Statikus oldalakon (Astro, Next, sima HTML — Claude Code-, v0-, Lovable-buildelve) más a logika: nincs központi admin, helyette **mikroszolgáltatások + külső API-k**. Egy funkciót gyakran többféle stack-en is megvalósíthatsz — itt segít eldönteni.

## Hosting + deploy
- **Deploy-szolgáltató:** Vercel, Netlify, Cloudflare Pages, GitHub Pages (mind ingyenes szinttel)
- **Domain:** helyi domain-regisztrátor, Namecheap, Cloudflare Registrar
- **SSL/HTTPS:** automatikus a deploy-szolgáltatónál
- **E-mail:** Google Workspace, ProtonMail Business, helyi mail-szolgáltató
- **Build-pipeline:** GitHub → Vercel/Netlify auto-deploy
- **CDN:** beépítve

## Form-kezelés (statikus oldalon űrlap)
- **Formspree, Basin, Web3Forms, Getform** — egyszerű kontakt, e-mailre küld
- **Formspark, Tally, Typeform** — multi-step, conditional logic
- **Saját Edge Function** (Vercel/Netlify/Cloudflare) — custom backend-logika
- **Email-továbbító** (Resend, Postmark, Mailgun, SendGrid)

## Hírlevél / feliratkozás
- **ActiveCampaign, Mailchimp, ConvertKit, MailerLite, Beehiiv, Substack** — embed-form vagy API
- **Brevo** — több piacon erős
- **Saját Supabase + Resend** — DIY teljes kontrollal

## Webáruház / e-commerce statikus oldalra
- **Stripe Checkout / Payment Links** — egytermékes vagy katalógus, statikus oldal is lehet shop
- **Snipcart, Foxy, Commerce Layer** — statikus oldalba beépíthető kosár
- **Shopify Buy Button** — beágyazható
- **Lemon Squeezy, Paddle, Gumroad** — Merchant of Record (helyi áfa-kérdést kezelik)
- **Saját Supabase + Stripe** — DIY full e-commerce

## Foglalási rendszer
- **Cal.com, Calendly, SimplyBook.me, TidyCal**
- **Acuity Scheduling, Setmore**

## CMS (ha mégis dinamikus tartalom kell)
- **Headless:** Sanity, Contentful, Strapi, Directus, Storyblok, Payload, Decap CMS, TinaCMS
- **Notion mint CMS:** Super.so, Potion, Bullet
- **Google Sheets mint CMS** — egyszerű adatokhoz
- **Markdown + Git** — fejlesztő-barát, statikus natívan

## Authentikáció / user-account
- **Clerk, Supabase Auth, Auth0, NextAuth.js, Better-Auth, AI-oprendszer**
- Magic link (Resend + JWT) — fejlesztőbarát
- Csak Google/Apple/GitHub-login — egyszerűsített

## Adatbázis / backend
- **Supabase, Neon, Turso** (Postgres)
- **PlanetScale** (MySQL)
- **MongoDB Atlas, Firebase Firestore**
- **Vercel KV, Upstash Redis** (key-value)
- **Convex** (real-time + auth integrálva)

## Search
- **Algolia, MeiliSearch, Typesense** — instant search
- **Pagefind** — statikusra natív build-időben generálódó kereső
- **Saját DB-keresés** (Supabase full-text)

## Komment / közösség
- **Giscus** (GitHub Discussions), **Cusdis, Utterances, Disqus, Hyvor Talk, Commento**
- **Tribe / Discord / Circle / Mighty Networks / Skool** — saját közösségi platform

## Chat / support
- **Crisp, Intercom, Tidio, Tawk.to, HubSpot Chat**
- **WhatsApp Business widget**
- **AI chatbot:** Voiceflow, Chatbase, custom OpenAI/Claude-integráció

## Analitika + tracking
- **GA4** (Google), **Plausible, Fathom, Umami** (privacy-first)
- **PostHog** (product + session-recording + A/B)
- **Microsoft Clarity** (heatmap, session-recording, ingyenes)
- **Meta Pixel, TikTok Pixel, Google Ads conversion** — hirdetésekhez
- **GTM** — tracking-orchestrátor

## SEO + meta
- **Astro/Next natív SEO** — meta-tagek, sitemap.xml, robots.txt build-időben
- **Schema.org JSON-LD** — strukturált adat (FAQ, LocalBusiness, Product, Review)
- **OpenGraph + Twitter card** — közösségi megosztás
- **Sitemap-submit** (Google Search Console, Bing)

## GDPR / cookie / adatvédelem
- **Cookiebot, CookieYes, Termly, Iubenda** — banner + privacy generator
- **Saját banner** + Plausible/Fathom (ezekhez nem kell cookie-banner)

## Akadálymentesség
- **axe DevTools, Lighthouse, WAVE** — audit
- **NVDA, VoiceOver-tesztelés**
- **WCAG 2.1 AA** — baseline cél

## AI-funkciók
- **AI chatbot a saját tartalomra** (RAG) — Voiceflow, Chatbase, custom Claude/OpenAI + vector DB (Pinecone, Supabase pgvector)
- **AI-generált personalized landing** — ipari-szegmensre szabva
- **AI-szöveg-generálás user-input alapján** (kvíz-eredmény, ajánlás, kalkuláció)
- **Smart form** — AI értelmezi a választ és vezet tovább
- **Voice-input form** (Whisper)
- **AI keresés** (semantic search a saját tartalomra)

## Konverzió-optimalizáló elemek
- **Lead magnet letöltő-form** — checklist, PDF, mini-tanfolyam
- **Webinar-regisztráció** — Demio, Crowdcast, WebinarJam vagy Cal.com + Zoom + saját landing
- **Quiz-funnel** — Interact, ScoreApp, Outgrow, custom
- **Visszaszámláló** (urgency)
- **Exit-intent popup** (OptinMonster, ConvertBox, Sleeknote)
- **Social proof popup** (Provely, FOMO, Useproof)
- **Sticky CTA + floating action button**
- **Affiliate-tracking** (Tapfiliate, Rewardful, FirstPromoter)

## Online kurzus / membership statikus alternatívák
- **Podia, Teachable, Thinkific, Kajabi** — hosztolt LMS
- **MemberSpace, Memberstack** — paywall bármilyen statikus oldalra
- **Outseta** — all-in-one (member + subscription + CRM + helpdesk)
- **Mighty Networks, Circle, Skool** — community + course
- **Saját Supabase + Stripe + privát oldalak** — DIY

## Helyi-piac-specifikus

Ha a célpiac helyi (nem nemzetközi), mindig említsd a helyi megoldásokat is. Példa-kategóriák, amiket helyi szolgáltatóval érdemes lefedni:

- **Online számlázás** — helyi, jogszabály-kompatibilis számlázó-szolgáltató
- **Bankkártyás fizetés** — helyi payment gateway vagy Stripe lokalizálva
- **Szállítás / csomagpont** — helyi futár- és csomagpont-hálózat
- **Adóhatóság-integráció** — automatikus számla-adat-jelentés, ha kötelező
- **GDPR / adatvédelmi template** — a helyi jognak megfelelő szöveggel

> A konkrét szolgáltatókat a brand-kontextusból (pl. `01-nyers/`, ha van ilyen fájl) vagy a felhasználó válaszaiból töltsd ki a célpiac szerint. Ha nincs adat, kérdezd meg, melyik országra / piacra tervezel.

## Mikor érdemes statikus / AI-builder stack-et javasolni

- Vállalkozói honlap (1-5 oldal) gyors megoldásra
- Landing pages, kampány-oldalak
- Modern, gyors, jó SEO a fő szempont
- Kevés szerkesztő, kevés admin-feladat
- AI-builder workflow (Claude Code / v0 / Lovable) része a stratégiának
- Kis költségvetés (Vercel/Netlify free tier elég)
- Tech-affin tulajdonos vagy fejlesztő-háttér van
