import path from "path";
import prisma from "../../../../lib/prisma";
import { mkdir, writeFile } from "fs/promises";
//import { write } from "fs";
export async function GET() {
  const items = await prisma.tracks.findMany();
  return Response.json(items);
}
//post para obter imagens
export async function POST(resquest: Request) {
  const formData = await resquest.formData();

  const file = formData.get("cover");
  //condição para verificar se o arquivo é do tipo imagem
  if (!(file instanceof File)) {
    return Response.json({ msg: "Arquivo inválido!" }, { status: 400 });
  }
  const arrayBuffer = await file.arrayBuffer();
  const buffer = Buffer.from(arrayBuffer);

  const uploeadDir = path.join(process.cwd(), "public", "uploads"); //aqui pode processar o arquivo, como salvar em um diretório ou banco de dados, nesta caso será craido no publi um uploads
  await mkdir(uploeadDir, { recursive: true });
  const filepath = path.join(uploeadDir, file.name); //construido o caminho public/uploads/nome do arquivo(no meu caso bando1)
  await writeFile(filepath, buffer);
  //agor é necessário armazenar no caminho o buffer
  //resposta como preferencia para viralizar os testes
  return Response.json({
    msg: "Dados recebidos com sucesso! ",
    filepath: `/public/uploads/${file.name}`,
  });
}

//JSON (abordagem)
// export async function POST(request: Request) {
//   const data = await request.json();
//   return Response.json({ msg: "Dados recebidos com sucesso ", data: { data } }); //data como é o nome da varável podia ter colocado apenas data
// }

// //URL enconded (abordagem)
// export async function POST(request: Request) {
//   const bodyTest = await request.text();
//   const params = new URLSearchParams(bodyTest);
//   const name = params.get("name");
//   const slug = params.get("slug");
//   const description = params.get("description");
//   const status = params.get("status");
//   //armazenar os dados no banco de dados
//   return Response.json({
//     msg: "Dados recebidos com sucesso ",
//     data: { name, slug, description, status },
//   });
// }
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
