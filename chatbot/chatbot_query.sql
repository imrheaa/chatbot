-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2021 at 07:33 AM
-- Server version: 10.1.39-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `chatbot_query`
--

-- --------------------------------------------------------

--
-- Table structure for table `new_query`
--

CREATE TABLE `new_query` (
  `S.N` int(10) NOT NULL,
  `Query` text NOT NULL,
  `Entry_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `new_query`
--

INSERT INTO `new_query` (`S.N`, `Query`, `Entry_at`) VALUES
(1, 'Rose is red', '2021-10-21 08:52:31'),
(3, 'green color', '2021-10-21 09:09:55'),
(9, 'white house', '0000-00-00 00:00:00'),
(10, 'red house', '2021-10-21 10:00:13'),
(11, 'red panda', '2021-10-21 10:01:03'),
(12, 'red panda', '2021-10-21 10:01:43'),
(13, 'haha', '2021-10-21 10:07:38'),
(14, 'sky is blue', '2021-10-21 10:08:01');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `new_query`
--
ALTER TABLE `new_query`
  ADD PRIMARY KEY (`S.N`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `new_query`
--
ALTER TABLE `new_query`
  MODIFY `S.N` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
