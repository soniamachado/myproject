export function SignupBanner() {
  return (
    <div className="mx-2 mb-4 flex items-center justify-between rounded-lg bg-gradient-to-r from-[#af2896] to-[#509bf5] px-4 py-3 lg:mx-4 lg:px-6">
      <div>
        <p className="text-xs font-medium text-foreground lg:text-sm">
          Preview of Spotify
        </p>
        <p className="text-sm font-bold text-foreground lg:text-base">
          Sign up to get unlimited songs and podcasts with occasional ads. No
          credit card needed.
        </p>
      </div>
      <a
        href="#"
        className="ml-4 flex-shrink-0 rounded-full bg-foreground px-6 py-3 text-sm font-bold text-background transition-transform hover:scale-105"
      >
        Sign up free
      </a>
    </div>
  );
}
