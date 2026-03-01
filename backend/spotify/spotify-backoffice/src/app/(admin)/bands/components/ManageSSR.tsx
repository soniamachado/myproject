import Button from "@/app/components/Button";
import { Band } from "../../../../../prisma/generated/prisma/client";

const TableRow = ({ band }: { band: Band }) => {
  return (
    <tr>
      <td className="px-6 py-4 white-nowrap text-gray-800">{band.name}</td>
      <td className="px-6 py-4 white-nowrap text-gray-800">
        {band.description && band.description.length > 30
          ? `${band.description.slice(0, 30)}...`
          : band.description}
      </td>
      <td className="px-6 py-4 white-nowrap ">
        {band.status}
        <span className="inline-flex items-center px-2 py-0.5 rounded bg-green-100 text-green-800">
          {band.status}
        </span>
      </td>
      <td className="text-rigth font-sm space-x-4 whitespace-nowrap">
        <Button>Editar</Button>
        <Button>Excluir</Button>
      </td>
    </tr>
  );
};

export default async function ManageSSR() {
  const response = await fetch("http://localhost:3000/api/band");
  const bands: Band[] = await response.json();
  return (
    <section className="overflow-x-auto p-4">
      <header className="flex justify-end mb-4">
        <Button>Adicionar Banda</Button>
      </header>
      <table className="min-w-full border border-gray-200 round-sm overflow-hidden">
        <thead className="bg-gray-100 text-gray-50 uppercase text-left"></thead>

        <tr>
          <th scope="col" className="px-6 py-3">
            Nome
          </th>
          <th scope="col" className="px-6 py-3">
            Descrição
          </th>
          <th scope="col" className="px-6 py-3">
            Status
          </th>
          <th scope="col" className="px-6 py-3">
            Status
          </th>
          <th scope="col" className="px-6 py-3">
            Status
          </th>
        </tr>
        <tbody className="bg-white divide-y divide-gray-200">
          {Array.isArray(bands) && bands.length > 0 ? (
            bands.map((band) => <TableRow key={band.id} band={band} />)
          ) : (
            <tr>
              <td colSpan={3} className="text-center text-gray-500 py-4">
                Nenhuma registro cadastrada
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </section>
  );
}
