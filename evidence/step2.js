async function main(){
  const byText = (re, tag='button') => [...document.querySelectorAll(tag)].find(b=>re.test(b.innerText||''));
  const sleep = ms => new Promise(r=>setTimeout(r,ms));
  const r = byText(/^render$/i);
  if(!r) return 'no render button';
  if(r.disabled) return 'render disabled';
  r.click();
  for(let i=0;i<90;i++){
    await sleep(2000);
    const t = document.body.innerText;
    if(/published|watch\?v=|youtu\.be/i.test(t)) return 'done-ish';
    const btn = byText(/download|publish/i);
    if(btn) return 'result buttons: '+btn.innerText.trim();
  }
  return 'timeout';
}
main();
