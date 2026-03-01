/*
  Warnings:

  - You are about to drop the column `coverUrl` on the `tracks` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "bands" ADD COLUMN     "cover_url" TEXT;

-- AlterTable
ALTER TABLE "tracks" DROP COLUMN "coverUrl";
