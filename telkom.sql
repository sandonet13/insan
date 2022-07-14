-- phpMyAdmin SQL Dump
-- version 4.9.5deb2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 14, 2022 at 06:59 PM
-- Server version: 10.3.34-MariaDB-0ubuntu0.20.04.1
-- PHP Version: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `telkom`
--

-- --------------------------------------------------------

--
-- Table structure for table `campaign`
--

CREATE TABLE `campaign` (
  `id` int(20) NOT NULL,
  `user_id` int(20) NOT NULL,
  `nama_campaign` varchar(100) NOT NULL,
  `status_campaign` enum('Waiting Approval','Editing in Progress','Ongoing Campaign') NOT NULL,
  `type_campaign` enum('Online Campaigne','Offline Campaigne') NOT NULL,
  `phase_campaign` enum('Planning','Designing','Testing','Execute/Publish') NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `product_campaign` text NOT NULL,
  `tasks` text NOT NULL,
  `id_socmed` int(20) NOT NULL,
  `publish_plan` datetime NOT NULL,
  `caption` varchar(255) NOT NULL,
  `tag_people` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `campaign`
--

INSERT INTO `campaign` (`id`, `user_id`, `nama_campaign`, `status_campaign`, `type_campaign`, `phase_campaign`, `start_date`, `end_date`, `product_campaign`, `tasks`, `id_socmed`, `publish_plan`, `caption`, `tag_people`) VALUES
(5, 2, 'Penantian dimualiii', 'Waiting Approval', 'Online Campaigne', 'Planning', '2022-07-01 00:18:11', '2022-07-01 00:18:11', 'Online', 'Penantian Usai', 4, '2022-07-01 00:18:11', 'Online', 'Wow'),
(7, 6, 'Internet Pro Max', 'Waiting Approval', 'Online Campaigne', 'Planning', '2022-07-01 00:18:11', '2022-07-01 00:18:11', 'Online', 'Upload Twitter', 4, '2022-07-01 00:18:11', 'Online', '@Wow');

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `id` int(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `nama_lengkap` varchar(100) NOT NULL,
  `alamat` text NOT NULL,
  `kategori` enum('Makro','Mikro','Mini','Small') NOT NULL,
  `kategori_influencer` enum('Youtuber','Celebgram','TikTok''ers','Twittertian') NOT NULL,
  `foto_profil` varchar(255) NOT NULL,
  `instagram` tinyint(1) NOT NULL DEFAULT 0,
  `twitter` tinyint(1) NOT NULL DEFAULT 0,
  `facebook` tinyint(1) NOT NULL DEFAULT 0,
  `tiktok` tinyint(1) NOT NULL DEFAULT 0,
  `youtube` tinyint(1) NOT NULL DEFAULT 0,
  `instagram_link` varchar(255) NOT NULL,
  `twitter_link` varchar(255) NOT NULL,
  `facebook_link` varchar(255) NOT NULL,
  `tiktok_link` varchar(255) NOT NULL,
  `youtube_link` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`id`, `user_id`, `nama_lengkap`, `alamat`, `kategori`, `kategori_influencer`, `foto_profil`, `instagram`, `twitter`, `facebook`, `tiktok`, `youtube`, `instagram_link`, `twitter_link`, `facebook_link`, `tiktok_link`, `youtube_link`) VALUES
(2, 2, 'Jane Hooper', 'Jl. Wijaya No. 23 Jakarta Selatan', 'Mikro', 'Youtuber', 'https://thumb.viva.co.id/media/frontend/thumbs3/2020/07/17/5f11a2b26f625-reza-darmawangsa_1265_711.jpeg', 0, 1, 1, 1, 1, 'https://www.instagram.com/rezadarmawangsa', 'https://twitter.com/tvindonesiawkwk', 'https://www.facebook.com/RZD-1841680799458709/', 'https://www.tiktok.com/@rzdarmawangsa', 'https://www.youtube.com/c/RZDarmawangsa'),
(4, 6, 'Lorep Ipsum Lengkap Sekali', 'Jl. Mojokerto Gang Bakti No. 20', 'Makro', 'Celebgram', 'http://google.com/image/foto.jpg', 0, 0, 0, 0, 0, '', '', '', '', ''),
(5, 10, 'Lorep Ipsum Lengkap Sekali', 'Jl. Mojokerto Gang Bakti No. 20', 'Makro', 'Celebgram', 'http://google.com/image/foto.jpg', 0, 0, 0, 0, 0, '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `socmed`
--

CREATE TABLE `socmed` (
  `id` int(20) NOT NULL,
  `socmed` varchar(20) NOT NULL,
  `api` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `socmed`
--

INSERT INTO `socmed` (`id`, `socmed`, `api`) VALUES
(1, 'Instagram', ''),
(2, 'Twitter', ''),
(3, 'Facebook', ''),
(4, 'TikTok', ''),
(5, 'Youtube', '');

-- --------------------------------------------------------

--
-- Table structure for table `token_blocklist`
--

CREATE TABLE `token_blocklist` (
  `id` int(100) NOT NULL,
  `jti` text NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `token_blocklist`
--

INSERT INTO `token_blocklist` (`id`, `jti`, `created_at`) VALUES
(4, 'bc397975-b837-4c36-86ea-2ebcd5acb822', '2022-07-14 11:57:37'),
(5, 'bc397975-b837-4c36-86ea-2ebcd5acb822', '2022-07-14 16:03:45'),
(6, 'bc397975-b837-4c36-86ea-2ebcd5acb822', '2022-07-14 16:03:52');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `roles` varchar(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `no_telp` varchar(20) NOT NULL,
  `user_id_telegram` varchar(20) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `roles`, `email`, `no_telp`, `user_id_telegram`, `password`, `created_at`, `updated_at`) VALUES
(2, 'cooper131', 'Supervisor', 'cooper131@gmail.com', '08124545124', '@cooper131', 'cooperaja123', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(3, 'Anjay', 'Contributor', 'anjay131@gmail.com', '0812454545', '@anjay13', 'pbkdf2:sha256:260000$SLQjwtKk3kvKJtw5$bd0ce72b68dbaa6065a0e6c446f9975d84a41636c93d942271e0a10dccfa896b', '2022-07-13 09:30:11', '2022-07-13 09:30:11'),
(4, 'johndoe123', 'Contributor', 'johndoe@gmail.com', '08565644544', '@johndoe', 'pbkdf2:sha256:260000$mKMpQUia7yZuiKoz$e0b5fd02e6835c5997c87cc37231d8b37e0778e8d57793db6a61f5afd20fc6a1', '2022-07-14 03:37:23', '2022-07-14 03:37:23'),
(6, 'loremipsum212', 'Moderator', 'loremipsum@gmail.com', '08122122455', '@loremipsum', 'pbkdf2:sha256:260000$bEfIZAejpEMPhWji$d12b3e5d9e58561e082431c610ef8eaea8f339424fef79740633bb659f8587b2', '2022-07-14 06:17:29', '2022-07-14 06:17:29');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `campaign`
--
ALTER TABLE `campaign`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `socmed`
--
ALTER TABLE `socmed`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `token_blocklist`
--
ALTER TABLE `token_blocklist`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `campaign`
--
ALTER TABLE `campaign`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `profile`
--
ALTER TABLE `profile`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `token_blocklist`
--
ALTER TABLE `token_blocklist`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
