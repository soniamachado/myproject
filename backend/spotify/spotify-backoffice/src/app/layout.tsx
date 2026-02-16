import "@radix-ui/themes/styles.css";
import "./globals.css";
//import { Theme } from "@radix-ui/themes";
//import Header from "./components/Header";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="pt-BR">
      <body>
        {/* <div className="border-4 border-blue-800">
          <Header />
          <Theme appearance="dark"> {children}</Theme>
        </div> */}
        {children}
      </body>
    </html>
  );
}
