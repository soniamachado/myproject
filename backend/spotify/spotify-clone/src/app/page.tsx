import { Sidebar } from "@/app/components/sidebar";
import { MainContent } from "@/app/components/main-content";
import { PlayerBar } from "@/app/components/player-bar";

export default function Page() {
  return (
    <div className="flex h-dvh flex-col bg-background">
      <div className="flex min-h-0 flex-1 gap-2 p-2">
        <Sidebar />
        <MainContent />
      </div>
      <PlayerBar />
    </div>
  );
}
