async function main(){
  const sleep = ms => new Promise(r=>setTimeout(r,ms));
  const byText = re => [...document.querySelectorAll('button')].find(b=>re.test(b.innerText||''));
  const pub = byText(/^publish$/i);
  if(!pub) return 'no publish button';
  pub.click();
  for(let i=0;i<60;i++){
    await sleep(2000);
    const m = document.body.innerText.match(/https:\/\/youtu\.be\/[A-Za-z0-9_-]+/);
    if(m) return m[0];
  }
  return 'publish timeout';
}
main();
