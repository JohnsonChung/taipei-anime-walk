import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

// https://astro.build/config
export default defineConfig({
  site: 'https://johnsonchung.github.io',
  base: '/taipei-anime-walk',
  output: 'static',
  integrations: [tailwind({ applyBaseStyles: false })]
});
