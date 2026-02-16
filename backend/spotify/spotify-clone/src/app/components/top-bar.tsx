"use client";

import { ChevronLeft, ChevronRight, Bell, Users } from "lucide-react";
import { SpotifyLogo } from "./spotify-logo";

export function TopBar() {
  return (
    <header className="flex items-center justify-between px-4 py-3 lg:px-6">
      <div className="flex items-center gap-4">
        <a href="#" aria-label="Spotify" className="text-foreground">
          <SpotifyLogo className="h-8 w-8" />
        </a>
        <div className="flex items-center gap-2">
          <button
            type="button"
            className="rounded-full bg-background/70 p-1.5 text-muted-foreground transition-colors hover:text-foreground disabled:opacity-40"
            aria-label="Go back"
            disabled
          >
            <ChevronLeft className="h-5 w-5" />
          </button>
          <button
            type="button"
            className="rounded-full bg-background/70 p-1.5 text-muted-foreground transition-colors hover:text-foreground disabled:opacity-40"
            aria-label="Go forward"
            disabled
          >
            <ChevronRight className="h-5 w-5" />
          </button>
        </div>

        {/* Search bar */}
        <div className="hidden items-center gap-2 rounded-full bg-secondary px-4 py-2.5 md:flex">
          <svg
            className="h-5 w-5 text-muted-foreground"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
          >
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <span className="text-sm text-muted-foreground">
            What do you want to play?
          </span>
        </div>
      </div>

      <div className="flex items-center gap-2">
        <a
          href="#"
          className="hidden rounded-full border border-muted-foreground/40 px-4 py-1.5 text-sm font-bold text-muted-foreground transition-all hover:scale-105 hover:border-foreground hover:text-foreground md:block"
        >
          Explore Premium
        </a>
        <a
          href="#"
          className="hidden items-center gap-1.5 rounded-full bg-foreground px-4 py-1.5 text-sm font-bold text-background transition-transform hover:scale-105 md:flex"
        >
          <svg className="h-4 w-4" viewBox="0 0 24 24" fill="currentColor">
            <path d="M17 1.01L7 1c-1.1 0-2 .9-2 2v18c0 1.1.9 2 2 2h10c1.1 0 2-.9 2-2V3c0-1.1-.9-1.99-2-1.99zM17 19H7V5h10v14z" />
          </svg>
          Install App
        </a>
        <button
          type="button"
          className="hidden rounded-full p-2 text-muted-foreground transition-colors hover:text-foreground md:block"
          aria-label="Notifications"
        >
          <Bell className="h-5 w-5" />
        </button>
        <button
          type="button"
          className="hidden rounded-full p-2 text-muted-foreground transition-colors hover:text-foreground md:block"
          aria-label="Friend activity"
        >
          <Users className="h-5 w-5" />
        </button>

        <div className="flex items-center gap-3">
          <a
            href="#"
            className="px-2 py-1 text-sm font-bold text-muted-foreground transition-colors hover:scale-105 hover:text-foreground"
          >
            Sign up
          </a>
          <a
            href="#"
            className="rounded-full bg-foreground px-6 py-2.5 text-sm font-bold text-background transition-transform hover:scale-105"
          >
            Log in
          </a>
        </div>
      </div>
    </header>
  );
}
