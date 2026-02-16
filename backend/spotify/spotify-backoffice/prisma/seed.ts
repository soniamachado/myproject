import { PrismaClient } from "../generated/prisma";
const prisma = new PrismaClient();
async function main() {
  await prisma.band.create({
    data: {
      name: "The Beatles",
      slug: "the-beatles",
      status: "ACTIVE",
      tracks: {
        create: [
          { title: "Hey Jude", slug: "hey-jude", duration: 431 },
          { title: "Let It Be", slug: "let-it-be", duration: 243 },
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
