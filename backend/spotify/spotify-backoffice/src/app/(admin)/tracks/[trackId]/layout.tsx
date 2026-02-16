import { ReactNode } from "react";

interface Props {
  children: ReactNode;
}
export default function Layout({ children }: Props) {
  return (
    <div className="border-4 border-yellow-800">
      <h1>TrackId Layout</h1>
      {children}
    </div>
  );
}
