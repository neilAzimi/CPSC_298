'use client'

import Link from 'next/link';
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { ArrowRight, BarChart, RefreshCcw, ShoppingBag, Users } from "lucide-react"
import './landing-page.css'; // Import the CSS file

export function LandingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-black text-white">
      <header className="px-4 lg:px-6 h-14 flex items-center bg-gray-900">
        <Link className="flex items-center justify-center" href="#">
          <ShoppingBag className="h-6 w-6 text-white" />
          <span className="ml-2 text-2xl font-bold">UniTrade</span>
        </Link>
        <nav className="ml-auto flex gap-4 sm:gap-6">
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Features
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            How It Works
          </Link>
          <Link className="text-sm font-medium hover:underline underline-offset-4" href="#">
            Testimonials
          </Link>
        </nav>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none animated-title">
                  Trade Groceries & Supplies with Fellow Students
                </h1>
                <p className="mx-auto max-w-[700px] text-gray-300 md:text-xl text-center">
                  UniTrade connects you with other students to exchange what you need. Save money, reduce waste, and
                  build community.
                </p>
              </div>
              <div className="space-x-4 flex justify-center">
                <Button className="inline-flex h-9 items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary disabled:pointer-events-none disabled:opacity-50">
                  Get Started
                </Button>
                <Button variant="outline">Learn More</Button>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-800">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12">Key Features</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              <Card className="bg-gray-700">
                <CardHeader>
                  <CardTitle>Easy Trading</CardTitle>
                </CardHeader>
                <CardContent>
                  <RefreshCcw className="h-12 w-12 mb-4 text-white" />
                  <p className="text-gray-300">Quickly find and trade items with other students on your campus.</p>
                </CardContent>
              </Card>
              <Card className="bg-gray-700">
                <CardHeader>
                  <CardTitle>Save Money</CardTitle>
                </CardHeader>
                <CardContent>
                  <BarChart className="h-12 w-12 mb-4 text-white" />
                  <p className="text-gray-300">Reduce your expenses by trading instead of buying new items.</p>
                </CardContent>
              </Card>
              <Card className="bg-gray-700">
                <CardHeader>
                  <CardTitle>Build Community</CardTitle>
                </CardHeader>
                <CardContent>
                  <Users className="h-12 w-12 mb-4 text-white" />
                  <p className="text-gray-300">Connect with fellow students and create a supportive network.</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12">How It Works</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="flex flex-col items-center text-center">
                <div className="rounded-full bg-primary text-primary-foreground p-3 mb-4">1</div>
                <h3 className="text-xl font-bold mb-2">List Your Items</h3>
                <p className="text-gray-300">Add the groceries or supplies you&apos;re willing to trade.</p>
              </div>
              <div className="flex flex-col items-center text-center">
                <div className="rounded-full bg-primary text-primary-foreground p-3 mb-4">2</div>
                <h3 className="text-xl font-bold mb-2">Find What You Need</h3>
                <p className="text-gray-300">Browse listings from other students on your campus.</p>
              </div>
              <div className="flex flex-col items-center text-center">
                <div className="rounded-full bg-primary text-primary-foreground p-3 mb-4">3</div>
                <h3 className="text-xl font-bold mb-2">Make the Trade</h3>
                <p className="text-gray-300">Connect and exchange items with fellow students.</p>
              </div>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-800">
          <div className="container px-4 md:px-6">
            <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center mb-12">What Students Say</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <Card className="bg-gray-700">
                <CardContent className="flex flex-col items-center text-center p-6">
                  <img
                    src="/placeholder.svg?height=100&width=100"
                    alt="Student 1"
                    className="rounded-full mb-4"
                    width={100}
                    height={100}
                  />
                  <p className="mb-2 text-gray-300">
                    &quot;UniTrade has been a game-changer! I&apos;ve saved so much money on groceries and made new friends in the
                    process.&quot;
                  </p>
                  <p className="font-bold">- Sarah, Junior</p>
                </CardContent>
              </Card>
              <Card className="bg-gray-700">
                <CardContent className="flex flex-col items-center text-center p-6">
                  <img
                    src="/placeholder.svg?height=100&width=100"
                    alt="Student 2"
                    className="rounded-full mb-4"
                    width={100}
                    height={100}
                  />
                  <p className="mb-2 text-gray-300">
                    &quot;I love how easy it is to find what I need. UniTrade has made campus life so much more convenient!&quot;
                  </p>
                  <p className="font-bold">- Mike, Sophomore</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl text-center">
                  Ready to Start Trading?
                </h2>
                <p className="mx-auto max-w-[600px] text-gray-300 md:text-xl text-center">
                  Join UniTrade today and start exchanging groceries and supplies with fellow students on your campus.
                </p>
              </div>
              <div className="space-x-4 flex justify-center">
                <Button className="inline-flex h-9 items-center justify-center rounded-md bg-primary px-4 py-2 text-sm font-medium text-primary-foreground shadow transition-colors hover:bg-primary/90 focus-visible:outline-none focus-visible:ring-1 focus-visible:ring-primary disabled:pointer-events-none disabled:opacity-50">
                  Sign Up Now
                  <ArrowRight className="ml-2 h-4 w-4" />
                </Button>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="flex flex-col gap-2 sm:flex-row py-6 w-full shrink-0 items-center px-4 md:px-6 border-t border-gray-600">
        <p className="text-xs text-gray-500">© 2023 UniTrade. All rights reserved.</p>
        <nav className="sm:ml-auto flex gap-4 sm:gap-6">
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Terms of Service
          </Link>
          <Link className="text-xs hover:underline underline-offset-4" href="#">
            Privacy
          </Link>
        </nav>
      </footer>
    </div>
  )
}
