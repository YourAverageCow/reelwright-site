async function main(){
  const setVal = (el, v) => {
    const proto = el.tagName === 'TEXTAREA' ? HTMLTextAreaElement.prototype : HTMLInputElement.prototype;
    Object.getOwnPropertyDescriptor(proto, 'value').set.call(el, v);
    el.dispatchEvent(new Event('input', {bubbles:true}));
    el.dispatchEvent(new Event('change', {bubbles:true}));
  };
  const byText = (re, tag='button') => [...document.querySelectorAll(tag)].find(b=>re.test(b.innerText||''));
  const sleep = ms => new Promise(r=>setTimeout(r,ms));

  const premise = document.querySelector('input[placeholder^="A night nurse"]');
  setVal(premise, "A night nurse finds a letter dated tomorrow, in her own handwriting.");
  await sleep(600);
  const gen = byText(/generate story/i);
  if(!gen) return 'no generate button';
  gen.click();

  for(let i=0;i<60;i++){
    await sleep(2000);
    const story = document.querySelector('textarea[placeholder^="Paste or write"]');
    if(story && story.value.length > 300) return 'story ready:'+story.value.length;
  }
  return 'story timeout';
}
main();
