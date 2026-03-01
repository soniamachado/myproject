/*
  Warnings:

  - You are about to drop the column `cover_url` on the `bands` table. All the data in the column will be lost.

*/
-- AlterTable
ALTER TABLE "bands" DROP COLUMN "cover_url",
ADD COLUMN     "coverUrl" TEXT NOT NULL DEFAULT 'uploads/default.jpg';

-- AlterTable
ALTER TABLE "tracks" ADD COLUMN     "coverUrl" TEXT NOT NULL DEFAULT 'uploads/default.jpg';
