-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2022 at 07:22 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `live`
--

-- --------------------------------------------------------

--
-- Table structure for table `emp`
--

CREATE TABLE `emp` (
  `Id` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `Mobile` varchar(20) DEFAULT NULL,
  `Address` varchar(20) DEFAULT NULL,
  `Dob` varchar(20) DEFAULT NULL,
  `Country` varchar(20) DEFAULT NULL,
  `Email` varchar(20) DEFAULT NULL,
  `Marriedstatus` varchar(20) DEFAULT NULL,
  `Qualification` varchar(20) DEFAULT NULL,
  `Gender` varchar(20) DEFAULT NULL,
  `Dept` varchar(20) DEFAULT NULL,
  `Salary` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `emp`
--

INSERT INTO `emp` (`Id`, `Name`, `Mobile`, `Address`, `Dob`, `Country`, `Email`, `Marriedstatus`, `Qualification`, `Gender`,`Dept`, `Salary`) VALUES
('1', 'LOKESH PATIL', '8974664666', 'JANAKI NAGAR', '4-6-1999', 'INDIA', 'lokesh@gmail.com', 'Unmarried', 'Computer Engineer','Male' 'A', '25000'),
('2', 'PARESH MAHAJAN', '7894766633', 'JOSHI PETH', '8-12-2000', 'INDIA', 'paresh78@gmail.com', 'Married', 'BTech','Male', 'A', '30000'),
('3', 'BHAVESH MALI', '7864423452', 'JIJAU NAGAR', '7-11-1998', 'INDIA', 'bhavesh18@gmail.com', 'Married', 'BTech','Male' ,'Developer', '35000'),
('4', 'RAJASHREE KAPURE', '7693747575', 'JALGAON', '3-7-1999', 'INDIA', 'rajashree147@gmail.c', 'Unmarried', 'Computer Engineer','Female', 'Computer', '30000');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
