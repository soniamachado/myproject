// interface Props {
//   params: {
//     trackId: string;
//   };
// }
// export async function Page(params: Props) {
//   const p = await params;

interface Props {
  params: Promise<{
    trackId: string;
  }>;

  searchParams: Promise<{
    mode: string;
    showTitle: string;
    anotherParam: string;
  }>;
}

export default async function Page({ params, searchParams }: Props) {
  const p = await params;
  const trackId = p.trackId;
  const sP = await searchParams;
  const mode = sP.mode;
  const showTitle = sP.showTitle;
  const anotherParam = sP.anotherParam;
  return (
    <>
      <h1>Musicas ID: {trackId}</h1>;<h2>Mode: {mode}</h2>;
      <h2>Show Title: {showTitle}</h2>;<h2>Another Param: {anotherParam}</h2>
    </>
  );
}
