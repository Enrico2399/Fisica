# Piramide dell'esame: righe dal basso (0) verso l'alto. Ogni mattone:
# id, t (titolo), a (area: mat/mec/ter/ele/ott/esa), f (formula KaTeX), d (spiegazione breve),
# fs (sezione del formulario), top (indice del macroargomento negli esercizi), dep (mattoni su cui poggia)
P = [
 [  # 0 Strumenti
  {"id":"m1","t":"Unità SI e conversioni","a":"mat","f":"\\text{km/h}\\div3{,}6\\quad T_K=T_C+273{,}15\\quad 1\\,\\text{cal}=4{,}186\\,\\text{J}","d":"È il cemento di tutta la piramide: un dato lasciato in cm, °C o km/h rovina anche il ragionamento giusto. Prima di ogni calcolo porta tutto in SI.","fs":1,"top":None,"dep":[]},
  {"id":"m2","t":"Vettori","a":"mat","f":"A_x=A\\cos\\theta,\\ A_y=A\\sin\\theta,\\ |\\vec A|=\\sqrt{A_x^2+A_y^2}","d":"Forze, velocità e campi sono frecce: si sommano per componenti, mai sommando i moduli.","fs":1,"top":1,"dep":[]},
  {"id":"m3","t":"Trigonometria","a":"mat","f":"\\sin\\alpha,\\ \\cos\\alpha,\\ \\tan\\alpha","d":"Serve per proiettare: il peso sul piano inclinato, la velocità nel moto parabolico, il flusso con l'angolo.","fs":1,"top":None,"dep":[]},
  {"id":"m4","t":"Derivate e integrali","a":"mat","f":"v=\\frac{dx}{dt},\\quad W=\\int F\\,dx,\\quad \\int\\frac{dx}{x}=\\ln x","d":"La derivata dice quanto in fretta cambia qualcosa, l'integrale somma tanti pezzetti: lavoro, flusso, f.e.m.","fs":1,"top":None,"dep":[]},
  {"id":"m5","t":"Grafici e pendenze","a":"mat","f":"F=-\\frac{dU}{dx},\\quad W=\\text{area sotto } p(V)","d":"Leggere un grafico: la pendenza è la derivata, l'area è l'integrale (esercizio 8.2, cicli termodinamici).","fs":1,"top":None,"dep":["m4"]},
  {"id":"m6","t":"Analisi dimensionale","a":"mat","f":"[\\text{N}]=[\\text{kg}\\cdot\\text{m/s}^2],\\ [\\text{J}]=[\\text{N}\\cdot\\text{m}]","d":"Il controllo più veloce: se il risultato non ha le unità giuste, c'è un errore nei passaggi.","fs":1,"top":None,"dep":["m1"]},
  {"id":"m7","t":"Equazioni e sistemi","a":"mat","f":"ax^2+bx+c=0,\\quad e^{-t/\\tau}\\Rightarrow t=\\tau\\ln(\\dots)","d":"Gli strumenti algebrici per isolare l'incognita: secondo grado, sistemi 2×2, esponenziali e logaritmi.","fs":1,"top":None,"dep":[]},
 ],
 [  # 1 Concetti base
  {"id":"c1","t":"Cinematica 1D","a":"mec","f":"x=x_0+v_0t+\\tfrac12at^2,\\quad v^2=v_0^2+2a\\Delta x","d":"Il navigatore del corpo: dice dove si trova e quanto veloce va, senza chiedersi perché.","fs":2,"top":1,"dep":["m1","m4"]},
  {"id":"c2","t":"Moto nel piano","a":"mec","f":"x=v_0\\cos\\theta\\,t,\\quad y=v_0\\sin\\theta\\,t-\\tfrac12gt^2","d":"Due film proiettati insieme: in orizzontale moto uniforme, in verticale caduta libera.","fs":2,"top":1,"dep":["c1","m2","m3"]},
  {"id":"c3","t":"Moto circolare","a":"mec","f":"v=\\omega R,\\quad a_c=\\frac{v^2}{R}=\\omega^2R","d":"La velocità cambia direzione di continuo: serve sempre una spinta verso il centro.","fs":2,"top":1,"dep":["c1","m2"]},
  {"id":"c4","t":"Leggi di Newton","a":"mec","f":"\\sum\\vec F=m\\vec a","d":"Le forze non tengono in moto i corpi, ne cambiano il moto. Disegna le forze e proietta sugli assi.","fs":3,"top":2,"dep":["m2","m3"]},
  {"id":"c5","t":"Temperatura e calore","a":"ter","f":"Q=mc\\,\\Delta T,\\quad T_e=\\frac{\\sum m_ic_iT_i}{\\sum m_ic_i}","d":"Il calore passa dal caldo al freddo come acqua tra vasi comunicanti finché le temperature si pareggiano.","fs":7,"top":5,"dep":["m1"]},
  {"id":"c6","t":"Carica e Coulomb","a":"ele","f":"F=k\\frac{q_1q_2}{r^2},\\quad \\vec E=\\frac{\\vec F}{q}","d":"Una carica cambia lo spazio attorno a sé: il campo è la mappa delle forze che sentirebbe un'altra carica.","fs":9,"top":7,"dep":["m2"]},
 ],
 [  # 2 Leggi di conservazione
  {"id":"d1","t":"Forze: peso, attrito, molla","a":"mec","f":"P=mg,\\quad f=\\mu N,\\quad F=-kx","d":"Le forze che compaiono in quasi ogni esercizio di meccanica. L'attrito si oppone sempre allo scivolamento.","fs":3,"top":2,"dep":["c4"]},
  {"id":"d2","t":"Lavoro ed energia","a":"mec","f":"K_i+U_i=K_f+U_f,\\quad W=\\Delta K","d":"L'energia è una moneta che cambia valuta: se il testo chiede una velocità tra due posizioni, usa l'energia.","fs":3,"top":2,"dep":["c4","m4"]},
  {"id":"d3","t":"Quantità di moto, urti","a":"mec","f":"\\sum\\vec p=\\text{cost.},\\quad v'=\\frac{m_1v_1+m_2v_2}{m_1+m_2}","d":"Negli urti i corpi si passano la quantità di moto come una palla: il totale della squadra non cambia.","fs":3,"top":2,"dep":["c4","m7"]},
  {"id":"d4","t":"Gas perfetto","a":"ter","f":"pV=nRT,\\quad U=nc_VT","d":"La pressione è una grandinata di molecole sulle pareti; la temperatura dice quanto forte grandina.","fs":7,"top":5,"dep":["c5"]},
  {"id":"d5","t":"Campo e potenziale","a":"ele","f":"V=k\\frac qr,\\quad W=q\\,\\Delta V,\\quad \\Delta V=Ed","d":"Il potenziale è l'altitudine su una mappa: le cariche positive scendono, il campo indica la discesa più ripida.","fs":9,"top":7,"dep":["c6","m4"]},
  {"id":"d6","t":"Corrente e Ohm","a":"ele","f":"V=Ri,\\quad P=Ri^2,\\quad i=\\frac{\\mathcal E}{R+r}","d":"Un fiume di elettroni in un tubo con ostacoli: la tensione è il dislivello, la resistenza gli ostacoli, l'attrito scalda.","fs":11,"top":8,"dep":["d5"]},
 ],
 [  # 3 Leggi fondamentali
  {"id":"e1","t":"Oscillazioni e onde","a":"mec","f":"\\omega=\\sqrt{k/m},\\quad T=2\\pi\\sqrt{l/g},\\quad v=\\lambda f","d":"Un'altalena che scambia velocità e altezza; l'onda è la ola allo stadio: si muove la forma, non le persone.","fs":4,"top":6,"dep":["d1","d2","c3"]},
  {"id":"e2","t":"Momento e inerzia","a":"mec","f":"\\tau=I\\alpha,\\quad K=\\tfrac12I\\omega^2,\\quad I=I_{cm}+Md^2","d":"Il momento d'inerzia è la pigrizia a girare: più la massa è lontana dall'asse, più fatica fai.","fs":5,"top":3,"dep":["c3","c4"]},
  {"id":"e3","t":"Fluidi","a":"mec","f":"p=p_0+\\rho gh,\\quad S=\\rho V_{imm}g,\\quad Av=\\text{cost.}","d":"Più scendi, più acqua hai sopra; dove il tubo si stringe il fluido accelera e la pressione cala.","fs":6,"top":4,"dep":["d1","d2"]},
  {"id":"e4","t":"Primo principio","a":"ter","f":"\\Delta U=Q-W,\\quad pV^\\gamma=\\text{cost. (adiabatica)}","d":"L'energia interna è un conto in banca: il calore è un versamento, il lavoro del gas un prelievo.","fs":8,"top":5,"dep":["d2","d4"]},
  {"id":"e5","t":"Teorema di Gauss","a":"ele","f":"\\oint\\vec E\\cdot d\\vec A=\\frac{Q_{int}}{\\varepsilon_0}","d":"Un sacchetto chiuso conta solo la carica che ha dentro. Utile quando c'è simmetria: sfere, fili, piani.","fs":9,"top":7,"dep":["d5"]},
 ],
 [  # 4 Teoria avanzata
  {"id":"f1","t":"Corpo rigido e statica","a":"mec","f":"\\sum\\vec F=0,\\ \\sum\\vec\\tau=0,\\quad T=2\\pi\\sqrt{\\frac{I}{mgd}}","d":"Equilibrio: il corpo non scappa e non gira. Il pendolo fisico è un corpo rigido che oscilla attorno a un perno.","fs":5,"top":3,"dep":["e2","d1"]},
  {"id":"f2","t":"Secondo principio","a":"ter","f":"\\eta=1-\\frac{|Q_f|}{Q_c},\\quad \\eta_C=1-\\frac{T_f}{T_c},\\quad \\sum\\frac QT\\le0","d":"Il calore cade come una cascata; la macchina è un mulino che ne sfrutta solo una parte.","fs":8,"top":5,"dep":["e4"]},
  {"id":"f3","t":"Condensatori e dielettrici","a":"ele","f":"C=\\frac{\\varepsilon_0\\varepsilon_rA}{d},\\quad U=\\tfrac12CV^2","d":"Una diga di carica. Zone affiancate con la stessa tensione: parallelo; strati sovrapposti: serie.","fs":10,"top":7,"dep":["e5","d5"]},
  {"id":"f4","t":"Campo magnetico","a":"ele","f":"F=qvB,\\quad r=\\frac{mv}{qB},\\quad B=\\frac{\\mu_0i}{2\\pi r}","d":"Un volante, non un acceleratore: curva le cariche senza cambiarne la velocità. Lo generano le correnti.","fs":12,"top":9,"dep":["d6","c3"]},
  {"id":"f5","t":"Ottica","a":"ott","f":"n_1\\sin\\theta_1=n_2\\sin\\theta_2,\\quad d\\sin\\theta=m\\lambda","d":"La luce si piega cambiando mezzo (il bagnino che corre e nuota) e interferisce come le onde nello stagno.","fs":14,"top":13,"dep":["e1","m3"]},
 ],
 [  # 5 Argomenti d'esame
  {"id":"g1","t":"Rotolamento puro","a":"mec","f":"v=\\omega R,\\quad K=\\tfrac12\\left(M+\\frac I{R^2}\\right)v^2","d":"Il punto a terra è un perno fermo: la ruota fa un passo di compasso alla volta. Domanda D1a.","fs":5,"top":3,"dep":["f1","d2"]},
  {"id":"g2","t":"Cicli termodinamici","a":"ter","f":"TV^{\\gamma-1}=\\text{cost.},\\quad \\eta=1-\\frac{|Q_{ced}|}{Q_{ass}}","d":"Tratto per tratto: dove entra calore, dove esce, quali temperature mancano. Esercizio F1b.","fs":8,"top":5,"dep":["f2","e4"]},
  {"id":"g3","t":"Induzione (Faraday–Lenz)","a":"ele","f":"\\Phi=NBA\\cos\\theta,\\quad \\mathcal E=-\\frac{d\\Phi}{dt}","d":"Il circuito è conservatore: se cambi il flusso, risponde con una corrente che si oppone. Esercizio F2b.","fs":13,"top":10,"dep":["f4","d6"]},
  {"id":"g4","t":"Onde EM e Maxwell","a":"ott","f":"c=\\frac1{\\sqrt{\\varepsilon_0\\mu_0}},\\quad E=cB","d":"Una staffetta: E che varia genera B, B che varia genera E, e viaggiano insieme alla velocità della luce.","fs":14,"top":11,"dep":["g3","e1"]},
 ],
 [  # 6 Esercizi tipo
  {"id":"x1","t":"F1a · corpo rigido","a":"esa","f":"mgR=\\tfrac12I\\omega^2,\\quad T=2\\pi\\sqrt{\\frac{I}{mgd}}","d":"Disco con massa al bordo: conservazione dell'energia con il momento d'inerzia, poi piccole oscillazioni.","fs":5,"top":0,"dep":["g1","f1","e1"]},
  {"id":"x2","t":"F1b · termodinamica","a":"esa","f":"T_E=T_B\\left(\\frac{T_D}{T_C}\\right)^{\\gamma},\\quad \\eta\\simeq0{,}56","d":"Ciclo con gas biatomico: temperature in kelvin, temperature mancanti dalle adiabatiche, rendimento.","fs":8,"top":0,"dep":["g2"]},
  {"id":"x3","t":"F2a · elettrostatica","a":"esa","f":"C=\\frac{\\varepsilon_0}{d_1}(\\varepsilon_rA_1+2A_2),\\quad U=\\tfrac12CV^2","d":"Condensatore composto da disco e corona: due condensatori in parallelo, attenzione a raggio e diametro.","fs":10,"top":0,"dep":["f3"]},
  {"id":"x4","t":"F2b · induzione","a":"esa","f":"\\mathcal E=\\frac{NAB_0\\sin30^\\circ}{\\tau}e^{-t/\\tau},\\quad P=Ri^2","d":"Bobina in un campo che decresce: flusso con l'angolo giusto, f.e.m., corrente, potenza.","fs":13,"top":0,"dep":["g3","d6"]},
 ],
]
APEX = {"id":"ex","t":"ESAME","a":"esa","f":"4\\ \\text{esercizi}+4\\ \\text{domande}","d":"Il vertice regge solo se tutto sotto è solido. Se un esercizio non torna, scendi lungo i mattoni del suo colore fino a trovare quello che manca.","fs":0,"top":0,"dep":["x1","x2","x3","x4"]}
