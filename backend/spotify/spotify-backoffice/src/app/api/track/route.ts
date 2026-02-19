import prisma from "../../../../lib/prisma";
export async function GET() {
  const bands = await prisma.band.findMany();
  return Response.json(bands);
}
export async function POST() {
  return Response.json({ msg: "API Rest- método POST: " });
}
export async function PATCH() {
  return Response.json({ msg: "API Rest- método PATCH: " });
}
export async function PUT() {
  return Response.json({ msg: "API Rest- método PUT: " });
}
export async function DELETE() {
  return Response.json({ msg: "API Rest- método DELETE: " });
}
export function HEAD() {
  return Response.json({ msg: "API Rest- método HEAD: " });
}
export function OPTIONS() {
  return Response.json({ msg: "API Rest- método OPTIONS: " });
}
