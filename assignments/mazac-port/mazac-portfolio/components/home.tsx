'use client'

import Link from 'next/link'
import { Button } from "@/components/ui/button"
import { MoonIcon, SunIcon, SearchIcon, BarChartIcon } from 'lucide-react'
import { TechnologiesComponent } from './technologies'

export function Page() {
  return (
    <div className="min-h-screen flex flex-col">
      <header className="p-4">
        <nav className="flex items-center justify-between max-w-6xl mx-auto">
          <Link href="/" className="text-2xl font-bold">
            <BarChartIcon className="w-8 h-8" />
          </Link>
          <ul className="hidden md:flex space-x-4">
            <li><Link href="/" className="hover:text-gray-300">Home</Link></li>
            <li><Link href="/blog" className="hover:text-gray-300">Blog</Link></li>
            <li><Link href="/projects" className="hover:text-gray-300">Projects</Link></li>
            <li><Link href="/about" className="hover:text-gray-300">About</Link></li>
            <li><Link href="/resume" className="hover:text-gray-300">Resume</Link></li>
          </ul>
          <div className="flex items-center space-x-2">
            <Button variant="ghost" size="icon">
              <SearchIcon className="w-5 h-5" />
            </Button>
            <Button variant="ghost" size="icon">
              <BarChartIcon className="w-5 h-5" />
            </Button>
            <Button variant="ghost" size="icon">
              <SunIcon className="w-5 h-5" />
            </Button>
          </div>
        </nav>
      </header>
      <main className="flex-grow flex flex-col items-center justify-center text-center p-4">
        <div className="relative w-64 h-64 mb-8">
          <div className="absolute inset-0 bg-blue-500 rounded-full animate-pulse"></div>
          <div className="absolute inset-4 bg-blue-700 rounded-full animate-pulse delay-75"></div>
          <div className="absolute inset-8 bg-blue-900 rounded-full animate-pulse delay-150"></div>
        </div>
        <h1 className="text-5xl font-bold mb-4">Hi, I'm Jack!</h1>
        <p className="max-w-2xl mb-8 text-gray-300">
          Welcome to my cybersecurity-focused portfolio where I showcase my web development projects 
          and share insights on the latest in cybersecurity research. 
          Exploring the intersection of web technologies and digital security.
        </p>
        <Button>
          Get in Touch
        </Button>
      </main>
      <TechnologiesComponent />
    </div>
  )
}