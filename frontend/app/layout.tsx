import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Reqi - Requirements-Driven Web Application Generator',
  description: 'Define requirements and generate web applications',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}

