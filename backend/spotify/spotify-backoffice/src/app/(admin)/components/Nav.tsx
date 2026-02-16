"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

type NavVariant = "desktop" | "hamburger";

interface NavigationItem {
  name: string;
  href: string;
}

interface NavProps {
  navigation: NavigationItem[];
  variant?: NavVariant;
}

const variants = {
  desktop: "rounded-md px-3 py-2 text-sm font-medium",
  hamburger: "block rounded-md px-3 py-2 text-base font-medium",
} satisfies Record<NavVariant, string>;

export default function Nav({ navigation, variant = "desktop" }: NavProps) {
  const pathname = usePathname();

  return (
    <>
      {navigation.map((item) => {
        const isActive =
          pathname === item.href ||
          (item.href !== "/" && pathname.startsWith(item.href));

        return (
          <Link
            key={item.href}
            href={item.href}
            aria-current={isActive ? "page" : undefined}
            className={[
              isActive
                ? "bg-gray-950/50 text-white"
                : "text-gray-300 hover:bg-white/5 hover:text-white",
              variants[variant],
            ].join(" ")}
          >
            {item.name}
          </Link>
        );
      })}
    </>
  );
}
