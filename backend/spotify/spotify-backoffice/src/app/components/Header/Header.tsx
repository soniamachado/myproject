import sytles from "./Header.module.scss";
console.log(sytles);

export default function Header() {
  return (
    <div className={`${sytles.header}`}>
      Logo | <a href="#">Menu </a>
    </div>
  );
}
