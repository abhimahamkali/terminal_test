// Renders each .slide in slides.html to a 1080x1350 PNG.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
  await page.goto('file://' + path.join(__dirname, 'slides.html'));
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(800);
  const out = path.join(__dirname, 'build')  // intermediate PNGs; final files live in export/;
  require('fs').mkdirSync(out, { recursive: true });
  for (const id of ['s1', 's2', 's3', 's4']) {
    await page.locator('#' + id).screenshot({ path: path.join(out, id + '.png') });
  }
  await page.evaluate(() => { document.body.style.background = 'transparent'; });
  await page.locator('#s5overlay').screenshot({ path: path.join(out, 's5_overlay.png'), omitBackground: true });
  await browser.close();
})();
