import "dotenv/config";
import { PrismaClient } from "./generated/prisma/client";
import { PrismaPg } from "@prisma/adapter-pg";
import pg from "pg";

const pool = new pg.Pool({ connectionString: process.env.DATABASE_URL });
const adapter = new PrismaPg(pool);
const prisma = new PrismaClient({ adapter });
async function main() {
  await prisma.band.create({
    data: {
      name: "The Beatles",
      slug: "the-beatles",
      status: "active",
      tracks: {
        create: [
          { title: "Hey Jude", slug: "hey-jude", durationInSecond: 431 },
          { title: "Let It Be", slug: "let-it-be", durationInSecond: 243 },
        ],
      },
    },
  });
}
main()
  .then(async () => {
    await prisma.$disconnect();
  })
  .catch(async (e) => {
    console.error("Error seeding data:", e);
    await prisma.$disconnect();
    process.exit(1);
  });
