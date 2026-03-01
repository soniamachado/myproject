import path from "node:path";
import crypto from "node:crypto";
//import { format } from "path";
//import { BandArraySchema } from "@/app/schemas/band.schema";
import prisma from "../../../../lib/prisma";
import { mkdir, writeFile } from "node:fs/promises";
//import { xid } from "zod";
//import { write } from "fs";
import * as z from "zod";
import { BandSchema } from "@/app/schemas/band.schema";
import { PrismaClientInitializationError } from "@prisma/client/runtime/client";
import { CustomError } from "@/app/utils/CustomError";

export async function GET() {
  const items = await prisma.band.findMany();
  console.log("estou aqui Get", items);
  return Response.json(items);
}

//post para obter imagens FormData (abordagem)
export async function POST(request: Request) {
  try {
    const formData = await request.formData();
    console.log(formData);
    //agor é necessário armazenar no caminho o buffer
    //resposta como preferencia para viralizar os testes
    // return Response.json({
    //   msg: "Dados recebidos com sucesso! ",
    //   filepath: `/public/uploads/${formData.name}`,
    // });

    const data = {
      name: formData.get("name"),
      slug: formData.get("slug"),
      description: formData.get("description") || "",
      status: formData.get("status"),
      cover: formData.get("cover"),
    };

    const validatedData = BandSchema.parse(data);

    //Todo: Verificar se o registro já existe!
    const bandExists = await prisma.band.findFirst({
      where: { name: validatedData.name },
    });
    if (bandExists) {
      //se houver um objeto na classe em cima vai ser verdadeiro, ou seja, já existe um registro com o mesmo nome
      throw new CustomError("Registro com o mesmo nome já existe!", 409);
    }

    if (!(data.cover instanceof File)) {
      throw new CustomError("Tipo inválido de arquivo", 400);
    }
    const arrayBuffer = await data.cover.arrayBuffer();
    const buffer = Buffer.from(arrayBuffer);

    const uploeadDir = path.join(process.cwd(), "public", "uploads"); //aqui pode processar o arquivo, como salvar em um diretório ou banco de dados, nesta caso será craido no publi um uploads
    await mkdir(uploeadDir, { recursive: true });

    //define um nome único para o arquivo, através do node UUID, evitar 2 utilizadores enviarem documentos com mesmo nome
    const uniqueName = crypto.randomUUID();
    const extension = path.extname(data.cover.name);

    const fileName = `${uniqueName}${extension}`; //assim que o usuario requisitar vai ter um identificador único e a extensão, nome do arquivo

    const filepath = path.join(uploeadDir, fileName); //construido o caminho public/uploads/nome do arquivo(no meu caso bando1)
    await writeFile(filepath, buffer);

    //Inserir os dados no banco via prisma

    const insertedItem = await prisma.band.create({
      data: {
        name: validatedData.name,
        slug: validatedData.slug,
        description: validatedData.description,
        status: validatedData.status,
        coverUrl: fileName,
      },
    });
    return Response.json({
      msg: "FormData ",
      insertedItem,
      filepath: `/public/uploads/${data.cover.name}`,
    });
  } catch (error: unknown) {
    console.error("Erro capturado:", error);
    if (error instanceof z.ZodError) {
      return Response.json(
        { error: "Erro de validação", details: error.issues },
        { status: 400 },
      );
    }
    if (error instanceof PrismaClientInitializationError) {
      return Response.json(
        {
          error: "Erro de conexão com o banco de dados",
        },
        { status: 500 },
      );
    }
    if (error instanceof CustomError) {
      return Response.json(
        { error: error.message },
        { status: error.statusCode },
      ); //estado de 400 de conflito
    }

    if (error instanceof Error) {
      return Response.json(
        {
          error:
            "erro interno do servidor.Solicite para a equipa responsável a avaliação dds logs de erros !",
        },
        { status: 500 },
      );
    }
    console.log("Erro ao processar a requisição:", error);
    return Response.json(
      { error: "Erro desconhecido (erro interno do servidor)" },
      { status: 500 },
    );
  }
}

// //JSON (abordagem)
// export async function POST(request: Request) {
//   try {
//     const data = await request.json();
//     if (typeof data === "object" && data !== null) {
//       //tratar como objeto
//       const validatedData = BandSchema.parse(data);
//       return Response.json({
//         msg: "Dados recebidos com sucesso! ",
//         data: validatedData,
//       });
//     } else {
//       return Response.json({ msg: "Dados inválidos! " }, { status: 400 });
//     }
//   } catch (error: unknown) {
//     if (error instanceof SyntaxError) {
//       console.error(
//         "Erro de sintaxe  ao ler JSON do body da requisição:",
//         error.message,
//       );
//       return Response.json(
//         { error: "Conteudo (body) da requisição está inválido!" },
//         { status: 400 },
//       );
//     }
//     if (error instanceof z.ZodError) {
//       return Response.json(
//         { error: "Erro de validação", details: error.issues },
//         { status: 400 },
//       );
//     }
//     console.log("Erro ao processar a requisição:", error);
//     return Response.json(
//       { error: "Erro desconhecido (erro interno do servidor)" },
//       { status: 500 },
//     );
//   }
// }

// //URL enconded (abordagem)
// export async function POST(request: Request) {
//   try {
//     const bodyText = await request.text();
//     const params = new URLSearchParams(bodyText);
//     const name = params.get("name");
//     const slug = params.get("slug");
//     const description = params.get("description");
//     const status = params.get("status");

//     //Validação dos dados
//     const validatedData = BandSchema.parse({
//       name: name,
//       slug: slug,
//       description: description || "", //se description for nulo ou indefinido, atribui uma string vazia
//       status: status,
//     });
//     //armazenar os dados no banco de dados
//     return Response.json({
//       msg: "Dados recebidos com sucesso. Url Eoncoded",
//       validatedData,
//     });
//   } catch (error: unknown) {
//     if (error instanceof z.ZodError) {
//       return Response.json(
//         { error: "Erro de validação", details: error.issues },
//         { status: 400 },
//       );
//     }

//     console.error("Erro ao processar a requisição:", error);
//     return Response.json(
//       { error: "Erro desconhecido (erro interno do servidor" },
//       { status: 500 },
//     );
//   }
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
