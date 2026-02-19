# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Spotify-inspired monorepo containing three main components:

- **spotify-clone**: Public-facing music streaming application
- **spotify-backoffice**: Admin interface for managing bands and tracks
- **spotify-db**: PostgreSQL database container setup

All services run in Docker containers and communicate through a shared `spotify-network`.

## Development Commands

### Database Setup

From the [spotify-db](spotify-db/) directory:

```bash
docker compose up
```

This starts PostgreSQL 17.8 on port 5432.

### Spotify Clone (Frontend)

From the [spotify-clone](spotify-clone/) directory:

```bash
# Start with Docker
docker compose up

# Or run locally (after database is running)
npm install
npm run dev  # Runs on http://localhost:3000
npm run build
npm run lint
```

### Spotify Backoffice (Admin)

From the [spotify-backoffice](spotify-backoffice/) directory:

```bash
# Start with Docker
docker compose up  # Runs on http://localhost:3001

# Or run locally (after database is running)
npm install
npm run dev
npm run build
npm run lint

# Prisma commands
npx prisma generate         # Generate Prisma Client
npx prisma db push          # Push schema changes to database
npx prisma studio           # Open Prisma Studio GUI
npx prisma migrate dev      # Create and apply migrations
npx prisma db seed          # Seed database with initial data
```

## Architecture

### Database Schema (Prisma)

The database schema is located in [spotify-backoffice/prisma/schema.prisma](spotify-backoffice/prisma/schema.prisma):

- **Band**: Stores band information (id, name, slug, description, status)
- **Tracks**: Stores track information (id, title, slug, durationInSecond)
- Relationship: One Band has many Tracks (1:N)
- Prisma Client output: `./generated/prisma` (custom path)

### Spotify Clone Structure

- Next.js App Router with TypeScript
- Components in [src/app/components](spotify-clone/src/app/components/):
  - `sidebar.tsx`: Navigation sidebar
  - `top-bar.tsx`: Top navigation
  - `player-bar.tsx`: Music player controls
  - `music-card.tsx`: Individual music cards
  - `content-section.tsx`: Main content sections
  - `main-content.tsx`: Main content wrapper
  - `signup-banner.tsx`: Sign up promotional banner

### Spotify Backoffice Structure

- Next.js App Router with TypeScript and route groups
- **Route Groups**:
  - `(admin)`: Protected admin pages
    - [/home](<spotify-backoffice/src/app/(admin)/home/>): Dashboard
    - [/bands](<spotify-backoffice/src/app/(admin)/bands/>): Band management (list, detail)
    - [/tracks](<spotify-backoffice/src/app/(admin)/tracks/>): Track management (list, detail)
  - `(public)`: Public pages
    - [/login](<spotify-backoffice/src/app/(public)/login/>): Login, forgot password, reset password
- Shared components in [src/app/components](spotify-backoffice/src/app/components/)

### Docker Configuration

All three services use Docker:

- **Database**: Uses `postgres:17.8` image, exposes port 5432
- **Frontend & Backoffice**: Both use `node:24.13.0-alpine3.22`
- **Network**: All services connect to `spotify-network` (bridge driver)
- **Volumes**: Database uses named volume `spotify-db-volume`
- Development command: `npm install && npm run dev` (runs in containers)

### Environment Variables

Backoffice requires `.env` file (see [.env.example](spotify-backoffice/.env.example)):

```
DATABASE_URL="postgresql://<user>:<password>@<host>:<port>/<database>?schema=public"
```

## Tech Stack

### Spotify Clone

- Next.js 16.1.6
- React 19.2.3
- TypeScript 5
- TailwindCSS 4
- Lucide React (icons)

### Spotify Backoffice

- Next.js 16.1.6
- React 19.2.3
- TypeScript 5
- Prisma 7.4.0 with PostgreSQL adapter
- TailwindCSS 4
- Radix UI Themes
- Headless UI
- Heroicons
- Prettier 3.8.1

## Key Conventions

- **Prisma Models**: Use PascalCase (e.g., `Band`, `Tracks`)
- **Database Tables**: Use snake_case with plural names (e.g., `bands`, `tracks`)
- **Field Mapping**: camelCase in code, snake_case in database using `@map`
- **Status Enum**: `active` | `inactive`
- **Custom Prisma Output**: Generated client is in `./generated/prisma`, not default location
