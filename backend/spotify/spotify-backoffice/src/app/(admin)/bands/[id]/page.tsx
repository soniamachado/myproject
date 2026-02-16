"use client";

import { useParams, useSearchParams } from "next/navigation";

export default function Page() {
  const params = useParams<{ id: string }>();
  //agora usar o hook search por parte do next/navigation para pegar o id da url, em que é usado pelo cliente
  const searchParams = useSearchParams();
  const mode = searchParams.get("mode");
  const showTitle = searchParams.get("showTitle");
  const anotherParam = searchParams.get("anotherParam"); //neste caso é null não aparece no browser
  if (typeof window === "undefined") {
    console.log("Running on the server");
  } else {
    console.log("Running on the client");

    return (
      <>
        <h1>Bandas ID: {params.id}</h1>
        <h2>Mode: {mode}</h2>
        <h2>showTitle: {showTitle}</h2>
        <h2>anotherParam: {anotherParam}</h2>
      </>
    );
  }
}
