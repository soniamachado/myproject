"use client";

import { TopBar } from "./top-bar";
import { ContentSection } from "./content-section";
import { SignupBanner } from "./signup-banner";

const trendingSongs = [
  { title: "DtMF", subtitle: "Bad Bunny", imageUrl: "/covers/cover-1.jpg" },
  {
    title: "The Great Divide",
    subtitle: "Noah Kahan",
    imageUrl: "/covers/cover-2.jpg",
  },
  {
    title: "YUKON",
    subtitle: "Justin Bieber",
    imageUrl: "/covers/cover-3.jpg",
  },
  {
    title: "Man I Need",
    subtitle: "Olivia Dean",
    imageUrl: "/covers/cover-4.jpg",
  },
  {
    title: "WILDFLOWER",
    subtitle: "Billie Eilish",
    imageUrl: "/covers/cover-5.jpg",
  },
  {
    title: "Manchild",
    subtitle: "Sabrina Carpenter",
    imageUrl: "/covers/cover-6.jpg",
  },
  {
    title: "Ordinary",
    subtitle: "Alex Warren",
    imageUrl: "/covers/cover-7.jpg",
  },
];

const popularArtists = [
  {
    title: "Rihanna",
    subtitle: "Artist",
    imageUrl: "/covers/artist-1.jpg",
    isRound: true,
  },
  {
    title: "Lady Gaga",
    subtitle: "Artist",
    imageUrl: "/covers/artist-2.jpg",
    isRound: true,
  },
  {
    title: "Ed Sheeran",
    subtitle: "Artist",
    imageUrl: "/covers/artist-3.jpg",
    isRound: true,
  },
  {
    title: "Coldplay",
    subtitle: "Artist",
    imageUrl: "/covers/artist-4.jpg",
    isRound: true,
  },
  {
    title: "Billie Eilish",
    subtitle: "Artist",
    imageUrl: "/covers/artist-5.jpg",
    isRound: true,
  },
  {
    title: "Drake",
    subtitle: "Artist",
    imageUrl: "/covers/artist-6.jpg",
    isRound: true,
  },
  {
    title: "Taylor Swift",
    subtitle: "Artist",
    imageUrl: "/covers/artist-7.jpg",
    isRound: true,
  },
];

const popularAlbums = [
  {
    title: "HIT ME HARD AND SOFT",
    subtitle: "Billie Eilish",
    imageUrl: "/covers/cover-5.jpg",
  },
  {
    title: "Short n' Sweet",
    subtitle: "Sabrina Carpenter",
    imageUrl: "/covers/cover-6.jpg",
  },
  {
    title: "AM",
    subtitle: "Arctic Monkeys",
    imageUrl: "/covers/cover-1.jpg",
  },
  {
    title: "The Rise and Fall of a Midwest Princess",
    subtitle: "Chappell Roan",
    imageUrl: "/covers/cover-3.jpg",
  },
  {
    title: "Hamilton",
    subtitle: "Lin-Manuel Miranda",
    imageUrl: "/covers/cover-2.jpg",
  },
  {
    title: "I'm The Problem",
    subtitle: "Morgan Wallen",
    imageUrl: "/covers/cover-4.jpg",
  },
  {
    title: "Midnights",
    subtitle: "Taylor Swift",
    imageUrl: "/covers/cover-7.jpg",
  },
];

const popularRadio = [
  {
    title: "Drake Radio",
    subtitle: "With Kendrick Lamar, PARTYNEXTDOOR, DJ Khaled and more",
    imageUrl: "/covers/radio-1.jpg",
  },
  {
    title: "Arctic Monkeys Radio",
    subtitle: "With Cigarettes After Sex, Tame Impala, TV Girl and more",
    imageUrl: "/covers/radio-2.jpg",
  },
  {
    title: "Sabrina Carpenter Radio",
    subtitle: "With Chappell Roan, Tate McRae, Olivia Rodrigo and more",
    imageUrl: "/covers/radio-3.jpg",
  },
  {
    title: "Ed Sheeran Radio",
    subtitle: "With Maroon 5, Sam Smith, One Direction and more",
    imageUrl: "/covers/radio-1.jpg",
  },
  {
    title: "Fleetwood Mac Radio",
    subtitle: "With Elton John, Billy Joel, Eagles and more",
    imageUrl: "/covers/radio-2.jpg",
  },
  {
    title: "Fred again.. Radio",
    subtitle: "With Skepta, Sammy Virji, Barry Can't Swim and more",
    imageUrl: "/covers/radio-3.jpg",
  },
  {
    title: "Beyonce Radio",
    subtitle: "With The Pussycat Dolls, Alicia Keys, JAY-Z and more",
    imageUrl: "/covers/radio-1.jpg",
  },
];

const featuredCharts = [
  {
    title: "Top Songs - Global",
    subtitle:
      "Your weekly update of the most played tracks right now - Global.",
    imageUrl: "/covers/chart-1.jpg",
  },
  {
    title: "Top Songs - Brazil",
    subtitle:
      "Your weekly update of the most played tracks right now - Brazil.",
    imageUrl: "/covers/chart-2.jpg",
  },
  {
    title: "Top 50 - Global",
    subtitle: "Your daily update of the most played tracks right now - Global.",
    imageUrl: "/covers/chart-1.jpg",
  },
  {
    title: "Viral 50 - Global",
    subtitle: "Your daily update of the most viral tracks right now - Global.",
    imageUrl: "/covers/chart-2.jpg",
  },
  {
    title: "Top 50 - Brazil",
    subtitle: "Your daily update of the most played tracks right now - Brazil.",
    imageUrl: "/covers/chart-1.jpg",
  },
  {
    title: "Viral 50 - Brazil",
    subtitle: "Your daily update of the most viral tracks right now - Brazil.",
    imageUrl: "/covers/chart-2.jpg",
  },
  {
    title: "Top Songs - USA",
    subtitle: "Your weekly update of the most played tracks right now - USA.",
    imageUrl: "/covers/chart-1.jpg",
  },
];

export function MainContent() {
  return (
    <main className="flex min-h-0 flex-1 flex-col rounded-lg bg-gradient-to-b from-[#1a1a2e] via-card to-card">
      <TopBar />
      <div className="flex-1 overflow-y-auto px-3 pb-4 scrollbar-thin lg:px-6">
        <ContentSection title="Trending songs" items={trendingSongs} />
        <ContentSection title="Popular artists" items={popularArtists} />
        <ContentSection
          title="Popular albums and singles"
          items={popularAlbums}
        />
        <ContentSection title="Popular radio" items={popularRadio} />
        <ContentSection title="Featured Charts" items={featuredCharts} />
      </div>
      <SignupBanner />
    </main>
  );
}
