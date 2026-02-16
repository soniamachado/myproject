"use client";

import {
  Shuffle,
  SkipBack,
  SkipForward,
  Repeat,
  Play,
  Volume2,
  Maximize2,
  ListMusic,
  MonitorSpeaker,
  Mic2,
} from "lucide-react";

export function PlayerBar() {
  return (
    <footer className="flex h-[72px] items-center justify-between border-t border-border bg-background px-2 lg:h-[90px] lg:px-4">
      {/* Left: Now Playing */}
      <div className="flex w-[180px] items-center gap-3 lg:w-[30%]">
        <div className="h-14 w-14 flex-shrink-0 rounded bg-accent" />
        <div className="hidden min-w-0 lg:block">
          <p className="cursor-pointer truncate text-sm font-medium text-foreground hover:underline">
            -
          </p>
          <p className="cursor-pointer truncate text-xs text-muted-foreground hover:text-foreground hover:underline">
            -
          </p>
        </div>
      </div>

      {/* Center: Controls */}
      <div className="flex max-w-[722px] flex-1 flex-col items-center gap-1 px-4">
        <div className="flex items-center gap-3 lg:gap-5">
          <button
            type="button"
            className="text-muted-foreground transition-colors hover:text-foreground"
            aria-label="Shuffle"
          >
            <Shuffle className="h-4 w-4" />
          </button>
          <button
            type="button"
            className="text-muted-foreground transition-colors hover:text-foreground"
            aria-label="Previous"
          >
            <SkipBack className="h-5 w-5 fill-current" />
          </button>
          <button
            type="button"
            className="flex h-8 w-8 items-center justify-center rounded-full bg-foreground text-background transition-transform hover:scale-110"
            aria-label="Play"
          >
            <Play className="h-4 w-4 fill-current" />
          </button>
          <button
            type="button"
            className="text-muted-foreground transition-colors hover:text-foreground"
            aria-label="Next"
          >
            <SkipForward className="h-5 w-5 fill-current" />
          </button>
          <button
            type="button"
            className="text-muted-foreground transition-colors hover:text-foreground"
            aria-label="Repeat"
          >
            <Repeat className="h-4 w-4" />
          </button>
        </div>

        {/* Progress Bar */}
        <div className="flex w-full items-center gap-2">
          <span className="w-10 text-right text-xs text-muted-foreground">
            -:--
          </span>
          <div className="group relative h-1 flex-1 cursor-pointer rounded-full bg-muted">
            <div className="h-full w-0 rounded-full bg-foreground transition-colors group-hover:bg-primary" />
            <div className="absolute -top-1 left-0 hidden h-3 w-3 rounded-full bg-foreground shadow group-hover:block" />
          </div>
          <span className="w-10 text-xs text-muted-foreground">-:--</span>
        </div>
      </div>

      {/* Right: Extra Controls */}
      <div className="hidden items-center gap-2 lg:flex lg:w-[30%] lg:justify-end">
        <button
          type="button"
          className="text-muted-foreground transition-colors hover:text-foreground"
          aria-label="Now playing view"
        >
          <Mic2 className="h-4 w-4" />
        </button>
        <button
          type="button"
          className="text-muted-foreground transition-colors hover:text-foreground"
          aria-label="Queue"
        >
          <ListMusic className="h-4 w-4" />
        </button>
        <button
          type="button"
          className="text-muted-foreground transition-colors hover:text-foreground"
          aria-label="Connect to a device"
        >
          <MonitorSpeaker className="h-4 w-4" />
        </button>
        <div className="group flex items-center gap-1">
          <button
            type="button"
            className="text-muted-foreground transition-colors hover:text-foreground"
            aria-label="Volume"
          >
            <Volume2 className="h-4 w-4" />
          </button>
          <div className="relative h-1 w-24 cursor-pointer rounded-full bg-muted">
            <div className="h-full w-2/3 rounded-full bg-foreground transition-colors group-hover:bg-primary" />
            <div className="absolute -top-1 left-[66%] hidden h-3 w-3 -translate-x-1/2 rounded-full bg-foreground shadow group-hover:block" />
          </div>
        </div>
        <button
          type="button"
          className="ml-1 text-muted-foreground transition-colors hover:text-foreground"
          aria-label="Full screen"
        >
          <Maximize2 className="h-4 w-4" />
        </button>
      </div>
    </footer>
  );
}
