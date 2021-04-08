-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:8889
-- Generation Time: Feb 05, 2021 at 09:42 AM
-- Server version: 5.7.32
-- PHP Version: 7.4.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `Gestion de factures`
--

-- --------------------------------------------------------

--
-- Table structure for table `Apis_apimodel`
--

CREATE TABLE `Apis_apimodel` (
  `num_fact` varchar(25) NOT NULL,
  `coordonnees_client` varchar(150) NOT NULL,
  `coordonnees_entreprise` varchar(150) NOT NULL,
  `date_facture` date NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `quantite` int(11) NOT NULL,
  `prix_ht` double NOT NULL,
  `tva` double NOT NULL,
  `prix_ttc` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `Categorie`
--

CREATE TABLE `Categorie` (
  `Id_categorie` int(11) NOT NULL,
  `nom_cat` varchar(50) NOT NULL,
  `date_creation` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Categorie`
--

INSERT INTO `Categorie` (`Id_categorie`, `nom_cat`, `date_creation`) VALUES
(1, 'Achat', '2021-02-03'),
(2, 'Assurances', '2021-02-01'),
(3, 'Dépenses', '2021-02-01');

-- --------------------------------------------------------

--
-- Table structure for table `Facture`
--

CREATE TABLE `Facture` (
  `num_fact` varchar(25) NOT NULL,
  `coordonnees_client` varchar(150) NOT NULL,
  `coordonnees_entreprise` varchar(150) NOT NULL,
  `date_facture` date NOT NULL,
  `nom_produit` varchar(50) NOT NULL,
  `quantite` int(50) NOT NULL,
  `prix_ht` float NOT NULL,
  `tva` float NOT NULL,
  `prix_ttc` float NOT NULL,
  `RefId_categorie` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Facture`
--

INSERT INTO `Facture` (`num_fact`, `coordonnees_client`, `coordonnees_entreprise`, `date_facture`, `nom_produit`, `quantite`, `prix_ht`, `tva`, `prix_ttc`, `RefId_categorie`) VALUES
('202102MO', '4 allée Marcel-Proust', '200 Avenue de la République 92001 Nanterre', '2021-02-02', 'électricité', 1, 1500, 0.2, 1800, 3),
('202102TE', '20 rue de la Jungle', '200 avenue de la République 92000 Nanterre', '2021-02-04', 'Iphone 11', 2, 1285.89, 0.2, 1543.67, 1),
('202103LK', '200 Avenue de la République 92001 Nanterre', '1 place stalingrad 75019 Paris', '2021-05-05', 'fournitures de bureau', 10, 100, 0.2, 120, 1),
('202103TE', '9 allée de de Saint Jean', '8 allée de l\'université', '2021-02-03', 'Iphone 12', 1, 687.2, 0.2, 859, 1),
('202104FD', '7 allée des Buttes', '200 Avenue de la République 92001 Nanterre', '2021-04-07', 'gaz/eau', 1, 2000, 0.2, 2400, 3);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Apis_apimodel`
--
ALTER TABLE `Apis_apimodel`
  ADD PRIMARY KEY (`num_fact`);

--
-- Indexes for table `Categorie`
--
ALTER TABLE `Categorie`
  ADD PRIMARY KEY (`Id_categorie`);

--
-- Indexes for table `Facture`
--
ALTER TABLE `Facture`
  ADD PRIMARY KEY (`num_fact`),
  ADD KEY `RefId_categorie` (`RefId_categorie`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Categorie`
--
ALTER TABLE `Categorie`
  MODIFY `Id_categorie` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `Facture`
--
ALTER TABLE `Facture`
  ADD CONSTRAINT `facture_ibfk_1` FOREIGN KEY (`RefId_categorie`) REFERENCES `Categorie` (`Id_categorie`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
