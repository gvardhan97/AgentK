import "./globals.css";
export const metadata = { title: "AgentK", description: "Agentic RAG and MCP workspace" };
export default function RootLayout({children}: Readonly<{children: React.ReactNode}>) {
 return <html lang="en"><body>{children}</body></html>;
}
