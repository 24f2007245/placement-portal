import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { VitePWA } from 'vite-plugin-pwa'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    VitePWA({
      registerType: 'autoUpdate',
      devOptions: {
        enabled: true // allows PWA in development
      },
      manifest: {
        name: 'Placement Cell',
        short_name: 'PCell',
        description: 'Vue + Flask Placement Portal',
        theme_color: '#2980B9',
        background_color: '#ffffff',
        display: 'standalone',
        start_url: '/',
        icons: [
          {
            src: '/icons/image.png',
            sizes: '192x192',
            type: 'image/png'
          },
          {
            src: '/icons/image.png',
            sizes: '512x512',
            type: 'image/png'
          }
        ]
      }
    }),
    // vueDevTools(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
