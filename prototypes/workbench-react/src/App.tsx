import {useMemo,useState} from "react";
type Dim="business"|"product"|"technical";
type Kind="company"|"product"|"company_product";
type Section={id:string;label:string;mandatory:boolean;stars:number};
type Template={id:string;name:string;dims:Dim[];status:"validated"|"candidate";pages:string;sections:string[]};
const catalog:Template[]=[
 {id:"architecture-note",name:"Architecture Note",dims:["business","product","technical"],status:"candidate",pages:"5–10",sections:["Decision & scope","Operating model / system","Evidence & dependencies","Options & trade-offs","Risks and falsifiers","Recommendation & next step"]},
 {id:"one-pager",name:"One-Pager",dims:["business","product"],status:"validated",pages:"1",sections:["Decision","Context & evidence","Options","Risks","Next action"]},
 {id:"two-pager",name:"Two-Pager",dims:["business","product"],status:"validated",pages:"2",sections:["Executive synthesis","Company / product reality","Use cases & value","Evidence","Risks & alternatives","Decision"]},
 {id:"benchmarking",name:"Benchmark",dims:["business","product","technical"],status:"candidate",pages:"2–6",sections:["Question","Comparables & criteria","Evidence","Scoring with hard gates","Sensitivity","Recommendation"]},
 {id:"buy-side-gap-analysis",name:"Buy-side Gap Analysis",dims:["business","product","technical"],status:"candidate",pages:"4–8",sections:["Buyer decision","Current state","Gap map","Alternatives","Risks","Investment decision"]},
 {id:"diagnostic-reco-sellside",name:"Sell-side Diagnostic",dims:["business","product"],status:"validated",pages:"5–9",sections:["Market context","ICP / value proposition","Commercial model","Competition","Recommendations","Validation"]},
 {id:"opportunity-note-icp",name:"ICP Opportunity Note",dims:["business","product"],status:"validated",pages:"4–8",sections:["Account truth","Need / urgency","Evidence","Product fit","Risks & hard gates","Pilot decision"]},
 {id:"integration-note",name:"Integration Note",dims:["business","product","technical"],status:"candidate",pages:"3–7",sections:["Decision","Integration path","Ownership & controls","Options","Risks & exit","Pilot"]},
 {id:"strategic-market-note",name:"Strategic Market Note",dims:["business"],status:"candidate",pages:"5–7",sections:["Market drivers","Company exposure","Value chain","Economics","Strategic options","Risks & decision"]}
];
const immutableLabels=new Set(["Evidence","Risks","Risks & alternatives","Risks and falsifiers","Risks & hard gates","Risks & decision","Recommendation & next step","Decision"]);
const initial=(t:Template):Section[]=>t.sections.map((label,i)=>({id:t.id+"-s"+(i+1),label,mandatory:immutableLabels.has(label),stars:0}));
const names:Record<Dim,string>={business:"Business",product:"Product",technical:"Tech"};
export function App(){
 const [kind,setKind]=useState<Kind>("company");
 const [company,setCompany]=useState("");
 const [product,setProduct]=useState("");
 const [question,setQuestion]=useState("What decision should this note enable?");
 const [q,setQ]=useState("");
 const [dims,setDims]=useState<Dim[]>(["business"]);
 const [chosen,setChosen]=useState("two-pager");
 const [sections,setSections]=useState<Section[]>(()=>initial(catalog[2]));
 const [mode,setMode]=useState<"search"|"deepsearch">("search");
 const [message,setMessage]=useState("Prototype local : aucune API, recherche, backend, accès GitHub ou export documentaire n'est connecté.");
 const filtered=useMemo(()=>catalog.filter(t=>t.name.toLowerCase().includes(q.toLowerCase())||t.id.includes(q.toLowerCase())).filter(t=>dims.some(d=>t.dims.includes(d))),[q,dims]);
 const picked=catalog.find(x=>x.id===chosen)!;
 function pick(t:Template){setChosen(t.id);setSections(initial(t));setMessage("Le ToC de démonstration vient de ce prototype, pas d'un contrat de template officiel.");}
 function move(id:string,offset:number){const i=sections.findIndex(s=>s.id===id),j=i+offset;if(j<0||j>=sections.length)return;const next=[...sections];[next[i],next[j]]=[next[j],next[i]];setSections(next);}
 function star(id:string){setSections(x=>x.map(s=>s.id===id?{...s,stars:(s.stars+1)%4}:s));}
 function overlay(){return {schema_version:"0.1.0",subject:{kind,name:kind==="product"?product:kind==="company"?company:company+" / "+product},template_ref:{id:picked.id,version:"DEMO_ONLY",sha256:"0".repeat(64)},analysis_dimension:dims[0],generation_mode:"from-scratch",research_mode:mode==="search"?"search":"deepsearch",decision_question:question,toc:sections.map((s,i)=>({section_id:s.id,rank:i+1,stars:s.stars})),outputs:["md"]};}
 function download(){const payload=JSON.stringify(overlay(),null,2);const url=URL.createObjectURL(new Blob([payload],{type:"application/json"}));const a=document.createElement("a");a.href=url;a.download="business-notes-overlay-DEMO.json";a.click();URL.revokeObjectURL(url);setMessage("Overlay démonstration sauvegardé. Il n'est pas validé contre le manifest officiel ni prêt pour une recherche.");}
 const canPlan=(kind==="company"?!!company.trim():kind==="product"?!!product.trim():!!company.trim()&&!!product.trim())&&question.trim().length>7;
 return <div className="shell">
 <header><div><h1>Business Notes <small>workbench / prototype</small></h1><p>Research → Evidence → Coach → Decision Note</p></div><span className="demo">LOCAL DEMO • NO BACKEND</span></header>
 <div className="workspace">
  <aside className="panel"><h2>1. Étude</h2><label>Objet de recherche<select value={kind} onChange={e=>setKind(e.target.value as Kind)}><option value="company">Entreprise</option><option value="product">Produit</option><option value="company_product">Entreprise + produit</option></select></label>
  {kind!=="product"&&<label>Entreprise<input placeholder="Ex. Atlas Financial (fictif)" value={company} onChange={e=>setCompany(e.target.value)}/></label>}
  {kind!=="company"&&<label>Produit<input placeholder="Ex. Compliance Gateway" value={product} onChange={e=>setProduct(e.target.value)}/></label>}
  <label>Question de décision<textarea value={question} onChange={e=>setQuestion(e.target.value)} rows={3}/></label>
  <fieldset><legend>Mode de recherche cible</legend><label className="inline"><input type="radio" checked={mode==="search"} onChange={()=>setMode("search")}/> Search</label><label className="inline"><input type="radio" checked={mode==="deepsearch"} onChange={()=>setMode("deepsearch")}/> Deepsearch</label></fieldset>
  <div className="notice">Recherche antérieure / Obsidian : <strong>non connecté</strong>. Le futur runtime proposera Réutiliser, Actualiser ou Nouvelle étude.</div></aside>
  <main className="panel"><h2>2. Templates <small>{filtered.length} résultats</small></h2><label>Rechercher<input aria-label="Rechercher des templates" value={q} onChange={e=>setQ(e.target.value)} placeholder="Nom, format ou catégorie"/></label>
  <div className="filters">{(Object.keys(names) as Dim[]).map(d=><button key={d} className={dims.includes(d)?"pill active":"pill"} aria-pressed={dims.includes(d)} onClick={()=>setDims(v=>v.includes(d)?(v.length>1?v.filter(x=>x!==d):v):[...v,d])}>{names[d]}</button>)}</div>
  <div className="templates">{filtered.map(t=><button key={t.id} className={t.id===chosen?"template selected":"template"} onClick={()=>pick(t)}><strong>{t.name}</strong><span>{t.pages} pages · {t.status}</span><span>{t.dims.map(d=>names[d]).join(" / ")}</span></button>)}</div>
  <p className="muted">Tags de la maquette illustratifs. Certains `supported_dimensions` ne sont pas encore déclarés dans le manifest officiel.</p></main>
  <aside className="panel"><h2>3. Table des matières <small>Coach</small></h2><div className="selected"><strong>{picked.name}</strong><span>{picked.pages} pages</span></div><p className="muted">↑/↓ pour classer · ★ pour demander plus de profondeur. Sections obligatoires non supprimables.</p>
  <ol className="toc">{sections.map((s,i)=><li key={s.id}><div><strong>{s.label}</strong>{s.mandatory&&<em>Protégée</em>}</div><div className="controls"><button aria-label={`Remonter ${s.label}`} disabled={i===0} onClick={()=>move(s.id,-1)}>↑</button><button aria-label={`Descendre ${s.label}`} disabled={i===sections.length-1} onClick={()=>move(s.id,1)}>↓</button><button title="Cycle 0 à 3 étoiles" aria-label={`Importance ${s.label} ${s.stars} sur 3`} onClick={()=>star(s.id)} className="stars">{"★".repeat(s.stars)}{"☆".repeat(3-s.stars)}</button></div></li>)}</ol>
  <button className="secondary" onClick={()=>setSections(initial(picked))}>Réinitialiser le ToC</button></aside>
 </div>
 <footer><div><span className="status">{message}</span><span className="muted">{canPlan?"Intake local complet pour la démo":"Renseigner la cible et la question avant planification."}</span></div><div className="actions"><button onClick={download} disabled={!canPlan}>Enregistrer overlay JSON</button>{(["Word","PDF","HTML","MD"] as const).map(f=><button key={f} disabled title="Export non implémenté dans cette maquette">{f}</button>)}</div></footer>
 </div>
}
