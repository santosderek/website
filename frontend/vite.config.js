import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

const apiOrigin = 'http://127.0.0.1:8000';

export default defineConfig({
  plugins: [react()],
  base: '/',
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    emptyOutDir: true,
    manifest: true,
  },
  server: {
    proxy: {
      '/api': apiOrigin,
      '/resume': apiOrigin,
    },
  },
  test: {
    environment: 'jsdom',
    setupFiles: './src/test/setup.js',
  },
});
