"use client";

import { MusicCard } from "./music-card";

interface ContentItem {
  title: string;
  subtitle: string;
  isRound?: boolean;
}

interface ContentSectionProps {
  title: string;
  items: ContentItem[];
}

export function ContentSection({ title, items }: ContentSectionProps) {
  return (
    <section className="mb-6 lg:mb-8">
      <div className="mb-3 flex items-center justify-between lg:mb-4">
        <h2 className="text-xl font-bold text-foreground lg:text-2xl">
          {title}
        </h2>
        <a
          href="#"
          className="text-sm font-bold text-muted-foreground transition-colors hover:text-foreground hover:underline"
        >
          Show all
        </a>
      </div>
      <div className="grid grid-cols-2 gap-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 2xl:grid-cols-7 lg:gap-4">
        {items.map((item) => (
          <MusicCard
            key={item.title}
            title={item.title}
            subtitle={item.subtitle}
            isRound={item.isRound}
          />
        ))}
      </div>
    </section>
  );
}
