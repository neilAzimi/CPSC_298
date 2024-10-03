'use client'

import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import Image from 'next/image'

const technologies = [
  { name: 'TypeScript', icon: '/typescript.svg' },
  { name: 'Next.js', icon: '/nextjs.svg' },
  { name: 'Tailwind', icon: '/tailwind.svg' },
  { name: 'Jotai', icon: '/jotai.svg' },
  { name: 'Framer Motion', icon: '/framer-motion.svg' },
  { name: 'Python', icon: '/python.svg' },
  { name: 'FastAPI', icon: '/fastapi.svg' },
  { name: 'Docker', icon: '/docker.svg' },
  { name: 'PostgreSQL', icon: '/postgresql.svg' },
  { name: 'Redis', icon: '/redis.svg' },
]

const experiences = [
  {
    company: 'CyberSec Solutions',
    position: 'Senior Web Developer & Security Analyst',
    period: 'Jan 2023 - Present',
    description: 'Developing secure web applications and conducting penetration testing to identify vulnerabilities in client systems. Implementing robust security measures and best practices in web development.',
    technologies: ['React', 'Node.js', 'Python', 'Kali Linux', 'Burp Suite']
  },
  {
    company: 'WebTech Innovations',
    position: 'Full Stack Developer',
    period: 'Mar 2021 - Dec 2022',
    description: 'Built and maintained scalable web applications using modern JavaScript frameworks and cloud technologies. Focused on creating efficient, responsive, and secure web solutions for various clients.',
    technologies: ['Vue.js', 'Express.js', 'MongoDB', 'AWS', 'Docker']
  }
]

export function TechnologiesComponent() {
  return (
    <section className="py-16 bg-black text-white">
      <h2 className="text-4xl font-bold mb-8 text-gray-300">Technologies I've worked with</h2>
      
      <Tabs defaultValue="most-used" className="mb-16">
        <TabsList className="bg-gray-900 p-1 rounded-md">
          <TabsTrigger value="most-used" className="data-[state=active]:bg-blue-500 rounded px-4 py-2 text-sm">Most Used</TabsTrigger>
          <TabsTrigger value="languages" className="data-[state=active]:bg-blue-500 rounded px-4 py-2 text-sm">Languages</TabsTrigger>
          <TabsTrigger value="web-dev" className="data-[state=active]:bg-blue-500 rounded px-4 py-2 text-sm">Web Dev</TabsTrigger>
          <TabsTrigger value="ai-data" className="data-[state=active]:bg-blue-500 rounded px-4 py-2 text-sm">AI & Data Science</TabsTrigger>
          <TabsTrigger value="devops" className="data-[state=active]:bg-blue-500 rounded px-4 py-2 text-sm">DevOps & Tools</TabsTrigger>
        </TabsList>
        <TabsContent value="most-used" className="mt-4">
          <Card className="bg-gray-900 border-gray-800">
            <CardHeader>
              <CardTitle className="text-gray-400 text-sm">These are my most used technologies.</CardTitle>
            </CardHeader>
            <CardContent className="flex flex-wrap gap-4">
              {technologies.map((tech) => (
                <div key={tech.name} className="flex items-center justify-center w-16 h-16 bg-gray-800 rounded-lg hover:bg-gray-700 transition-colors">
                  <Image src={tech.icon} alt={tech.name} width={32} height={32} />
                </div>
              ))}
            </CardContent>
          </Card>
        </TabsContent>
        {/* Add other TabsContent for languages, web-dev, ai-data, and devops */}
      </Tabs>

      <h2 className="text-4xl font-bold mb-8 text-gray-300">Experience</h2>
      <div className="grid grid-cols-4 gap-4">
        <div className="col-span-1 space-y-2">
          {experiences.map((exp, index) => (
            <div key={index} className="bg-gray-900 rounded-lg p-3 cursor-pointer hover:bg-gray-800 transition-colors">
              <h3 className="font-semibold text-blue-400">{exp.company}</h3>
              <p className="text-gray-400 text-sm">{exp.position}</p>
            </div>
          ))}
        </div>
        <div className="col-span-3">
          <Card className="bg-gray-900 border-gray-800">
            <CardHeader>
              <CardTitle className="text-xl font-semibold">{experiences[0].company}</CardTitle>
              <p className="text-gray-400">{experiences[0].position}</p>
              <p className="text-gray-500 text-sm">{experiences[0].period}</p>
            </CardHeader>
            <CardContent>
              <p className="text-gray-300 mb-4">{experiences[0].description}</p>
              <div className="flex flex-wrap gap-2">
                {experiences[0].technologies.map((tech) => (
                  <span key={tech} className="px-2 py-1 bg-gray-800 rounded-full text-xs text-gray-300">
                    {tech}
                  </span>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>
      </div>
    </section>
  )
}