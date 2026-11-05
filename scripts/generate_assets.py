from pathlib import Path
from html import escape
import random

ROOT = Path(__file__).resolve().parents[1]
A = ROOT / 'assets'
random.seed(27)

def text(x,y,s,size=20,color='#eef6ff',weight=400,extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="Segoe UI, Arial, sans-serif" font-size="{size}" font-weight="{weight}" {extra}>{escape(s)}</text>'

DEFS='''<defs>
<linearGradient id="bg" x2="1" y2="1"><stop stop-color="#071326"/><stop offset=".52" stop-color="#10182e"/><stop offset="1" stop-color="#211337"/></linearGradient>
<linearGradient id="glass" x2=".9" y2="1"><stop stop-color="#cadfff" stop-opacity=".18"/><stop offset=".45" stop-color="#809acd" stop-opacity=".06"/><stop offset="1" stop-color="#d7b4ff" stop-opacity=".12"/></linearGradient>
<linearGradient id="edge" x2="1" y2="1"><stop stop-color="#b4f7ff" stop-opacity=".8"/><stop offset=".45" stop-color="#8793ce" stop-opacity=".15"/><stop offset="1" stop-color="#e0b9ff" stop-opacity=".65"/></linearGradient>
<linearGradient id="spectrum"><stop stop-color="#8af5ee"/><stop offset=".5" stop-color="#b6bbff"/><stop offset="1" stop-color="#f0afff"/></linearGradient>
<radialGradient id="aura"><stop stop-color="#578aff" stop-opacity=".4"/><stop offset="1" stop-color="#578aff" stop-opacity="0"/></radialGradient>
<radialGradient id="planet" cx=".3" cy=".25"><stop stop-color="#aaf3ff"/><stop offset=".3" stop-color="#627fa7"/><stop offset=".65" stop-color="#2c3c63"/><stop offset="1" stop-color="#10142c"/></radialGradient>
<filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>
<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="#c3d7ff" stroke-opacity=".045"/></pattern>
</defs>
<style>.orbit{transform-origin:934px 252px;animation:orbit 45s linear infinite}.pulse{animation:pulse 7s ease-in-out infinite}@keyframes orbit{to{transform:rotate(360deg)}}@keyframes pulse{50%{opacity:.45}}@media(prefers-reduced-motion:reduce){.orbit,.pulse{animation:none}}</style>'''

def panel(x,y,w,h,r=20):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="url(#glass)" stroke="url(#edge)"/>'

def svg(name,h,body,title):
    stars=''.join(f'<circle cx="{random.randrange(12,1188)}" cy="{random.randrange(10,h-10)}" r="{random.choice([.6,.9,1.2])}" fill="#d4e7ff" opacity="{random.uniform(.15,.5):.2f}"/>' for _ in range(80))
    out=f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{h}" viewBox="0 0 1200 {h}" role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{DEFS}<rect width="1200" height="{h}" rx="24" fill="url(#bg)"/><rect width="1200" height="{h}" rx="24" fill="url(#grid)"/>{stars}{body}</svg>'
    (A/name).write_text(out,encoding='utf-8')

b='<circle cx="930" cy="245" r="360" fill="url(#aura)"/>'
b+=text(48,50,'SS /',22,'#9af5ec',600)+text(111,50,'Sumit Saini',18,'#c4d0e3')
b+=text(1152,50,'New Delhi  /  DTU',17,'#c4d0e3',extra='text-anchor="end"')
b+='<path d="M48 73H1152" stroke="#a7baff" stroke-opacity=".18"/>'
# Orbital sculpture, with a translucent instrument plate in front.
b+='<g fill="none" stroke="url(#spectrum)"><ellipse cx="934" cy="252" rx="215" ry="78" transform="rotate(-32 934 252)" opacity=".55"/><ellipse cx="934" cy="252" rx="210" ry="135" transform="rotate(42 934 252)" opacity=".3"/><circle cx="934" cy="252" r="151" stroke-dasharray="1 12" opacity=".7"/><circle cx="934" cy="252" r="182" stroke-dasharray="90 24 2 24" class="orbit" opacity=".5"/></g>'
b+='<circle cx="934" cy="252" r="100" fill="url(#planet)"/><path d="M848 225Q933 180 1022 248M835 251Q930 220 1030 277M850 288Q940 269 1011 307" fill="none" stroke="#c1f6ff" stroke-opacity=".16"/>'
b+='<ellipse cx="934" cy="252" rx="215" ry="78" transform="rotate(-32 934 252)" fill="none" stroke="#8af5ee" stroke-width="2" stroke-dasharray="360 800"/><circle cx="1104" cy="150" r="5" fill="#9af5ec" class="pulse"/>'
b+=text(48,135,'AI, grounded in evidence.',22,'#abbbd2')
b+=text(43,220,'SUMIT',96,'#f3f7ff',700, 'letter-spacing="-3"')
b+=text(43,304,'SAINI',96,'#f3f7ff',700,'letter-spacing="-3"')
b+=text(48,357,'From data to intelligence.',30,'#9af5ec',500)
b+=text(48,397,'Built to be understood.',30,'#cdd7ee',500)
b+=panel(772,374,380,89,16)+text(795,409,'From raw data to real decisions.',19,'#edf6ff',600)+text(795,438,'Models / Retrieval / Decision support',15,'#bccce4')
b+=panel(48,464,680,105)+text(72,502,'AI / Machine learning / Data analytics',23,'#eef6ff',600)+text(72,538,'Delhi Technological University',20,'#bccce4')
b+=text(793,519,'Explore the work below',21,'#a9f1ed',500)+text(793,550,'Data. Systems. Possibility.',17,'#b7c5dc')
b+='<path d="M48 600H1152" stroke="url(#spectrum)" stroke-opacity=".55"/>'
svg('hero.svg',624,b,'Sumit Saini — AI / Machine learning / Data analytics at DTU. AI, machine learning and data analytics.')

projects=[('telecom.svg','Understand why customers leave.','Telecom Retention Intelligence','Python / XGBoost / SHAP / PostgreSQL','#8af5ee',['Churn analysis with held-out evaluation,','model explanations and SQL exploration.'],'air'),('voiceops.svg','Give conversations context.','VoiceOps / ZentroMart','Python / Retrieval / Speech interfaces','#efb3ff',['Policy-grounded support with verification,','conversation state and human handover.'],'film'),('cybersec.svg','Make experiments reproducible.','CyberSecMax','QLoRA / Qwen2.5 / Evaluation design','#ffce92',['A defensive cybersecurity fine-tuning pipeline.','Training and benchmark execution pending.'],'risk')]
for filename,headline,sub,stack,color,lines,kind in projects:
    p='<circle cx="1020" cy="140" r="300" fill="url(#aura)"/>'+panel(22,22,1156,226)
    p+=text(52,72,sub,29,'#f2f6ff',600)+text(52,110,headline,23,color,500)
    p+=text(52,148,lines[0],20,'#c3d0e5')+text(52,176,lines[1],20,'#c3d0e5')+text(52,220,stack,17,color)
    p+=panel(805,44,343,181,16)
    if kind=='air':
        p+=text(831,78,'Holdout ROC-AUC',18,'#d7e9fa')
        p+=text(831,129,'0.8465',44,color,600)
        p+=text(831,165,'XGBoost · 1,409 customers',17,'#d7e9fa')
        p+=text(831,197,'Repository evaluation result',15,'#b9c9df')
    elif kind=='film':
        p+=text(831,79,'Retrieve → Verify → Respond',17,'#d7e9fa')
        for i,v in enumerate([15,26,45,62,35,76,47,30,55,26,14,35,58,28]):
            p+=f'<rect x="{835+i*21}" y="{150-v/2}" width="6" height="{v}" rx="3" fill="{color}" opacity=".7"/>'
        p+=text(831,206,'Speech integration · API keys required',15,'#c6d2e9')
    else:
        p+=text(831,78,'A reproducible protocol',18,'#d7e9fa')
        for j,label in enumerate(['Baseline','Adapter','Evaluation']):
            p+=f'<circle cx="844" cy="{110+j*39}" r="5" fill="{color}"/>'
            p+=text(865,116+j*39,label,20,'#d7e9fa')
        p+='<path d="M844 115V144M844 154V183" stroke="#ffce92" stroke-opacity=".5"/>'
    svg(filename,270,p,headline+' '+sub+'. '+stack+'. Decorative illustration, not measured project data.')

b=text(42,55,'The toolkit',32,'#edf6ff',600)+text(1156,52,'Analysis → insight → application',19,'#b9c9e3',extra='text-anchor="end"')
for x,title,rows,c in [(40,'Data & computation',['Python · SQL','Pandas · NumPy · Jupyter'],'#8af5ee'),(423,'Machine learning',['XGBoost · scikit-learn','SHAP · Model evaluation'],'#efb3ff'),(806,'Applied AI & systems',['RAG · llama.cpp · GGUF','Git · PostgreSQL · Go'],'#ffce92')]:
    b+=panel(x,83,354,137,16)+text(x+23,119,title,22,c,600)+text(x+23,158,rows[0],20)+text(x+23,189,rows[1],18,'#c0cde3')
svg('toolkit.svg',248,b,'Toolkit: Python, SQL, Pandas, NumPy, Jupyter, XGBoost, scikit-learn, SHAP, RAG, llama.cpp, GGUF, Git, PostgreSQL and Go.')
b='<circle cx="1040" cy="80" r="280" fill="url(#aura)"/>'+text(44,67,'Let’s build something worth exploring.',36,'#edf6ff',600)+text(44,111,'AI, machine learning and data. Ideas with a practical purpose.',21,'#bccde3')
b+='<path d="M44 142H1156" stroke="url(#spectrum)"/>'
svg('footer.svg',170,b,'Let’s build something worth exploring. Connect with Sumit Saini.')
print('Created six self-contained SVG assets.')
