document$.subscribe(async () => {
  const elements = document.querySelectorAll('.mermaid')
  if (elements.length > 0) {
    mermaid.initialize({ startOnLoad: false })
    await mermaid.run({ nodes: elements })
  }
})
