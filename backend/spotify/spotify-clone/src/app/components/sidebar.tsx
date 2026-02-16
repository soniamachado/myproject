"use client";

import { Home, Search, Library, Plus, Globe, ArrowRight } from "lucide-react";

const playlists = [
  "Chill Vibes",
  "Workout Mix",
  "Focus Flow",
  "Road Trip",
  "Indie Discoveries",
  "Late Night Jazz",
  "Pop Hits 2025",
  "Rock Classics",
];

export function Sidebar() {
  return (
    <aside className="flex w-[72px] flex-col gap-2 lg:w-[340px]">
      {/* Navigation */}
      <nav className="rounded-lg bg-card px-3 py-2 lg:px-4 lg:py-4">
        <ul className="flex flex-col gap-2">
          <li>
            <a
              href="#"
              className="flex items-center gap-4 rounded-md px-2 py-2 text-foreground transition-colors hover:text-foreground lg:px-3"
            >
              <Home className="h-6 w-6" strokeWidth={2.5} />
              <span className="hidden text-base font-bold lg:block">Home</span>
            </a>
          </li>
          <li>
            <a
              href="#"
              className="flex items-center gap-4 rounded-md px-2 py-2 text-muted-foreground transition-colors hover:text-foreground lg:px-3"
            >
              <Search className="h-6 w-6" />
              <span className="hidden text-base font-bold lg:block">
                Search
              </span>
            </a>
          </li>
        </ul>
      </nav>

      {/* Library */}
      <div className="flex min-h-0 flex-1 flex-col rounded-lg bg-card">
        <div className="flex items-center justify-between px-3 py-2 lg:px-4 lg:py-4">
          <button
            type="button"
            className="flex items-center gap-3 text-muted-foreground transition-colors hover:text-foreground"
          >
            <Library className="h-6 w-6" />
            <span className="hidden text-base font-bold lg:block">
              Your Library
            </span>
          </button>
          <div className="hidden items-center gap-2 lg:flex">
            <button
              type="button"
              className="rounded-full p-1.5 text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
              aria-label="Create playlist or folder"
            >
              <Plus className="h-5 w-5" />
            </button>
            <button
              type="button"
              className="rounded-full p-1.5 text-muted-foreground transition-colors hover:bg-accent hover:text-foreground"
              aria-label="Show more"
            >
              <ArrowRight className="h-5 w-5" />
            </button>
          </div>
        </div>

        {/* Create Playlist / Podcast CTA */}
        <div className="hidden flex-1 flex-col gap-5 overflow-y-auto px-2 pb-4 scrollbar-thin lg:flex">
          <div className="rounded-lg bg-secondary p-4">
            <p className="mb-1 text-base font-bold text-foreground">
              Create your first playlist
            </p>
            <p className="mb-4 text-sm text-muted-foreground">
              {"It's easy, we'll help you"}
            </p>
            <button
              type="button"
              className="rounded-full bg-foreground px-4 py-1.5 text-sm font-bold text-background transition-transform hover:scale-105"
            >
              Create playlist
            </button>
          </div>
          <div className="rounded-lg bg-secondary p-4">
            <p className="mb-1 text-base font-bold text-foreground">
              {"Let's find some podcasts to follow"}
            </p>
            <p className="mb-4 text-sm text-muted-foreground">
              {"We'll keep you updated on new episodes"}
            </p>
            <button
              type="button"
              className="rounded-full bg-foreground px-4 py-1.5 text-sm font-bold text-background transition-transform hover:scale-105"
            >
              Browse podcasts
            </button>
          </div>

          {/* Playlists List */}
          <div className="flex flex-col gap-1">
            {playlists.map((name) => (
              <button
                type="button"
                key={name}
                className="flex items-center gap-3 rounded-md px-2 py-2 text-left transition-colors hover:bg-accent"
              >
                <div className="flex h-12 w-12 flex-shrink-0 items-center justify-center rounded bg-accent">
                  <svg
                    className="h-5 w-5 text-muted-foreground"
                    viewBox="0 0 24 24"
                    fill="currentColor"
                  >
                    <path d="M15 6H3v2h12V6zm0 4H3v2h12v-2zM3 16h8v-2H3v2zM17 6v8.18c-.31-.11-.65-.18-1-.18-1.66 0-3 1.34-3 3s1.34 3 3 3 3-1.34 3-3V8h3V6h-5z" />
                  </svg>
                </div>
                <div className="min-w-0">
                  <p className="truncate text-sm font-medium text-foreground">
                    {name}
                  </p>
                  <p className="text-xs text-muted-foreground">Playlist</p>
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* Footer Links */}
        <div className="hidden border-t border-border px-4 py-4 lg:block">
          <div className="mb-4 flex flex-wrap gap-x-3 gap-y-1">
            {[
              "Legal",
              "Safety & Privacy Center",
              "Privacy Policy",
              "Cookies",
              "About Ads",
              "Accessibility",
            ].map((link) => (
              <a
                key={link}
                href="#"
                className="text-[11px] text-muted-foreground hover:text-foreground"
              >
                {link}
              </a>
            ))}
          </div>
          <button
            type="button"
            className="flex items-center gap-1.5 rounded-full border border-muted-foreground px-3 py-1 text-sm font-bold text-foreground transition-colors hover:scale-105 hover:border-foreground"
          >
            <Globe className="h-4 w-4" />
            English
          </button>
        </div>
      </div>
    </aside>
  );
}
