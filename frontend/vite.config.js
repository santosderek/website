import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const flaskOrigin = 'http://127.0.0.1:8000';

export default defineConfig({
  plugins: [react()],
  base: '/static/spa/',
  build: {
    outDir: '../website/static/spa',
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
  },
  server: {
    proxy: {
      '/api': flaskOrigin,
      '/resume': flaskOrigin,
      '/github': flaskOrigin,
      '/linkedin': flaskOrigin,
      '/robots.txt': flaskOrigin,
      '/static': flaskOrigin,
    },
  },
  test: {
    environment: 'jsdom',
    setupFiles: './src/test/setup.js',
  },
});
