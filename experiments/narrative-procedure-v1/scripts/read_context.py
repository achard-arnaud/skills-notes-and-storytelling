import argparse,json,time,hashlib,re
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("--arm",required=True,choices=["A","B","B2"]);p.add_argument("paths",nargs="+");a=p.parse_args()
root=Path(__file__).resolve().parent
log=root/("out-"+a.arm)/"reads.jsonl";log.parent.mkdir(exist_ok=True)
for name in a.paths:
 path=(root/name).resolve()
 if not path.is_relative_to(root):raise SystemExit("outside experiment")
 raw=path.read_bytes();body=raw.decode("utf-8")
 with log.open("a") as f:f.write(json.dumps({"path":name,"bytes":len(raw),"words":len(re.findall(r"\S+",body)),"sha256":hashlib.sha256(raw).hexdigest(),"read_at":time.time()})+"\n")
 print("\nFILE "+name+"\n"+body)

