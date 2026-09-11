/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        paper: {
          DEFAULT: '#F9F8F6',
          card: '#FFFFFF',
          border: '#E8E5DF',
          hover: '#F2EFE9'
        },
        ink: {
          DEFAULT: '#22201E',
          muted: '#66615B',
          light: '#948E85'
        },
        accent: {
          DEFAULT: '#E05A47',
          hover: '#C84836',
          light: '#FCECE9'
        },
        archive: {
          DEFAULT: '#6B665E',
          stamp: '#8C4830',
          bg: '#EDEAE3'
        },
        walk: {
          blue: '#2B5C8F',
          green: '#3E7B5C'
        }
      },
      fontFamily: {
        sans: [
          '"Noto Sans TC"',
          '-apple-system',
          'BlinkMacSystemFont',
          '"Segoe UI"',
          'Roboto',
          'sans-serif'
        ],
        serif: [
          '"Noto Serif TC"',
          'source-han-serif-tc',
          'Georgia',
          'serif'
        ],
        mono: [
          'ui-monospace',
          'SFMono-Regular',
          'Menlo',
          'monospace'
        ]
      }
    },
  },
  plugins: [],
}
