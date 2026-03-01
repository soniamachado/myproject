import * as z from "zod";

import { BandArraySchema } from "@/app/schemas/band.schema";
//JSON (abordagem)
export async function POST(request: Request) {
  try {
    const data = await request.json();
    if (Array.isArray(data)) {
      const validatedData = BandArraySchema.parse(data);
      //TODO: Armazenar os dados no banco de dados
      return Response.json({
        msg: "JSON(array) recebido com sucesso! ",
        data: validatedData,
      });
      //tratar como array
    } else {
      return Response.json({ msg: "Dados inválidos! " }, { status: 400 });
    }
  } catch (error: unknown) {
    if (error instanceof SyntaxError) {
      console.error(
        "Erro de sintaxe  ao ler JSON do body da requisição:",
        error.message,
      );
      return Response.json(
        { error: "Conteudo (body) da requisição está inválido!" },
        { status: 400 },
      );
    }
    if (error instanceof z.ZodError) {
      return Response.json(
        { error: "Erro de validação", details: error.issues },
        { status: 400 },
      );
    }
    console.log("Erro ao processar a requisição:", error);
    return Response.json(
      { error: "Erro desconhecido (erro interno do servidor)" },
      { status: 500 },
    );
  }
}
