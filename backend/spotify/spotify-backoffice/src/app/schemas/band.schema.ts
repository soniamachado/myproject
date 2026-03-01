import * as z from "zod";

const MAX_SIZE_MB = 5;
const ACCEPT_TYPES = ["image/jpeg", "image/png"];
export const BandSchema = z.object({
  name: z.string().min(1, "O nome é obrigatório"), //MIN DE 1 catacter
  slug: z.string().min(1, "O slug é obrigatório"),
  description: z.string().optional(),
  status: z.enum(["active", "inactive"]),
  cover: z
    .instanceof(File)
    .refine((file) => file.size > 0, { message: "arquivo é obrigatório" })
    .refine((file) => file.size < MAX_SIZE_MB * 1024 * 1024, {
      message: `o tamanho máximo permitido de ${MAX_SIZE_MB} MB`,
    })
    .refine((file) => ACCEPT_TYPES.includes(file.type), {
      message: `Tipo inválido. Permitidos:${ACCEPT_TYPES.join(",")}`,
    }),
});

export const BandArraySchema = z.array(BandSchema).min(1);
