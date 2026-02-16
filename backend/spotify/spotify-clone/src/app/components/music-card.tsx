"use client";

interface MusicCardProps {
  title: string;
  subtitle: string;
  isRound?: boolean;
}

export function MusicCard({ title, subtitle, isRound }: MusicCardProps) {
  return (
    <button
      type="button"
      className="group flex flex-col gap-2 rounded-md bg-card/40 p-2 text-left transition-colors hover:bg-card"
    >
      <div
        className={`relative aspect-square w-full ${
          isRound ? "rounded-full" : "rounded-md"
        } bg-gradient-to-br from-emerald-500/60 via-sky-500/60 to-purple-500/60`}
      >
        <div className="flex h-full w-full items-center justify-center">
          <span className="text-3xl font-black uppercase text-background">
            {title.charAt(0)}
          </span>
        </div>
      </div>
      <div className="space-y-0.5">
        <p className="truncate text-sm font-semibold text-foreground">
          {title}
        </p>
        <p className="line-clamp-2 text-xs text-muted-foreground">{subtitle}</p>
      </div>
    </button>
  );
}
