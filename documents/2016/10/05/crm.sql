-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Aug 29, 2016 at 10:02 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.5.37

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `country`
--

CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `country` varchar(200) NOT NULL DEFAULT ''
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Dumping data for table `country`
--

INSERT INTO `country` (`id`, `country`) VALUES
(1, 'Afghanistan'),
(2, 'Åland Islands'),
(3, 'Albania'),
(4, 'Algeria'),
(5, 'American Samoa'),
(6, 'Andorra'),
(7, 'Angola'),
(8, 'Anguilla'),
(9, 'Antarctica'),
(10, 'Antigua and Barbuda'),
(11, 'Argentina'),
(12, 'Armenia'),
(13, 'Aruba'),
(14, 'Australia'),
(15, 'Austria'),
(16, 'Azerbaijan'),
(17, 'Bahamas'),
(18, 'Bahrain'),
(19, 'Bangladesh'),
(20, 'Barbados'),
(21, 'Belarus'),
(22, 'Belgium'),
(23, 'Belize'),
(24, 'Benin'),
(25, 'Bermuda'),
(26, 'Bhutan'),
(27, 'Bolivia'),
(28, 'Bosnia and Herzegovina'),
(29, 'Botswana'),
(30, 'Bouvet Island'),
(31, 'Brazil'),
(32, 'British Indian Ocean Territory'),
(33, 'Brunei Darussalam'),
(34, 'Bulgaria'),
(35, 'Burkina Faso'),
(36, 'Burundi'),
(37, 'Cambodia'),
(38, 'Cameroon'),
(39, 'Canada'),
(40, 'Cape Verde'),
(41, 'Cayman Islands'),
(42, 'Central African Republic'),
(43, 'Chad'),
(44, 'Chile'),
(45, 'China'),
(46, 'Christmas Island'),
(47, 'Cocos (Keeling) Islands'),
(48, 'Colombia'),
(49, 'Comoros'),
(50, 'Congo'),
(51, 'Congo, The Democratic Republic of the'),
(52, 'Cook Islands'),
(53, 'Costa Rica'),
(54, 'Côte D''Ivoire'),
(55, 'Croatia'),
(56, 'Cuba'),
(57, 'Cyprus'),
(58, 'Czech Republic'),
(59, 'Denmark'),
(60, 'Djibouti'),
(61, 'Dominica'),
(62, 'Dominican Republic'),
(63, 'Ecuador'),
(64, 'Egypt'),
(65, 'El Salvador'),
(66, 'Equatorial Guinea'),
(67, 'Eritrea'),
(68, 'Estonia'),
(69, 'Ethiopia'),
(70, 'Falkland Islands (Malvinas)'),
(71, 'Faroe Islands'),
(72, 'Fiji'),
(73, 'Finland'),
(74, 'France'),
(75, 'French Guiana'),
(76, 'French Polynesia'),
(77, 'French Southern Territories'),
(78, 'Gabon'),
(79, 'Gambia'),
(80, 'Georgia'),
(81, 'Germany'),
(82, 'Ghana'),
(83, 'Gibraltar'),
(84, 'Greece'),
(85, 'Greenland'),
(86, 'Grenada'),
(87, 'Guadeloupe'),
(88, 'Guam'),
(89, 'Guatemala'),
(90, 'Guernsey'),
(91, 'Guinea'),
(92, 'Guinea-Bissau'),
(93, 'Guyana'),
(94, 'Haiti'),
(95, 'Heard Island and McDonald Islands'),
(96, 'Holy See (Vatican City State)'),
(97, 'Honduras'),
(98, 'Hong Kong'),
(99, 'Hungary'),
(100, 'Iceland'),
(101, 'India'),
(102, 'Indonesia'),
(103, 'Iran, Islamic Republic of'),
(104, 'Iraq'),
(105, 'Ireland'),
(106, 'Isle of Man'),
(107, 'Israel'),
(108, 'Italy'),
(109, 'Jamaica'),
(110, 'Japan'),
(111, 'Jersey'),
(112, 'Jordan'),
(113, 'Kazakhstan'),
(114, 'Kenya'),
(115, 'Kiribati'),
(116, 'Korea, Democratic People''s Republic of'),
(117, 'Korea, Republic of'),
(118, 'Kuwait'),
(119, 'Kyrgyzstan'),
(120, 'Lao People''s Democratic Republic'),
(121, 'Latvia'),
(122, 'Lebanon'),
(123, 'Lesotho'),
(124, 'Liberia'),
(125, 'Libyan Arab Jamahiriya'),
(126, 'Liechtenstein'),
(127, 'Lithuania'),
(128, 'Luxembourg'),
(129, 'Macao'),
(130, 'Macedonia, The Former Yugoslav Republic of'),
(131, 'Madagascar'),
(132, 'Malawi'),
(133, 'Malaysia'),
(134, 'Maldives'),
(135, 'Mali'),
(136, 'Malta'),
(137, 'Marshall Islands'),
(138, 'Martinique'),
(139, 'Mauritania'),
(140, 'Mauritius'),
(141, 'Mayotte'),
(142, 'Mexico'),
(143, 'Micronesia, Federated States of'),
(144, 'Moldova, Republic of'),
(145, 'Monaco'),
(146, 'Mongolia'),
(147, 'Montenegro'),
(148, 'Montserrat'),
(149, 'Morocco'),
(150, 'Mozambique'),
(151, 'Myanmar'),
(152, 'Namibia'),
(153, 'Nauru'),
(154, 'Nepal'),
(155, 'Netherlands'),
(156, 'Netherlands Antilles'),
(157, 'New Caledonia'),
(158, 'New Zealand'),
(159, 'Nicaragua'),
(160, 'Niger'),
(161, 'Nigeria'),
(162, 'Niue'),
(163, 'Norfolk Island'),
(164, 'Northern Mariana Islands'),
(165, 'Norway'),
(166, 'Oman'),
(167, 'Pakistan'),
(168, 'Palau'),
(169, 'Palestinian Territory, Occupied'),
(170, 'Panama'),
(171, 'Papua New Guinea'),
(172, 'Paraguay'),
(173, 'Peru'),
(174, 'Philippines'),
(175, 'Pitcairn'),
(176, 'Poland'),
(177, 'Portugal'),
(178, 'Puerto Rico'),
(179, 'Qatar'),
(180, 'Reunion'),
(181, 'Romania'),
(182, 'Russian Federation'),
(183, 'Rwanda'),
(184, 'Saint Barthélemy'),
(185, 'Saint Helena'),
(186, 'Saint Kitts and Nevis'),
(187, 'Saint Lucia'),
(188, 'Saint Martin'),
(189, 'Saint Pierre and Miquelon'),
(190, 'Saint Vincent and the Grenadines'),
(191, 'Samoa'),
(192, 'San Marino'),
(193, 'Sao Tome and Principe'),
(194, 'Saudi Arabia'),
(195, 'Senegal'),
(196, 'Serbia'),
(197, 'Seychelles'),
(198, 'Sierra Leone'),
(199, 'Singapore'),
(200, 'Slovakia'),
(201, 'Slovenia'),
(202, 'Solomon Islands'),
(203, 'Somalia'),
(204, 'South Africa'),
(205, 'South Georgia and the South Sandwich Islands'),
(206, 'Spain'),
(207, 'Sri Lanka'),
(208, 'Sudan'),
(209, 'Suriname'),
(210, 'Svalbard and Jan Mayen'),
(211, 'Swaziland'),
(212, 'Sweden'),
(213, 'Switzerland'),
(214, 'Syrian Arab Republic'),
(215, 'Taiwan, Province Of China'),
(216, 'Tajikistan'),
(217, 'Tanzania, United Republic of'),
(218, 'Thailand'),
(219, 'Timor-Leste'),
(220, 'Togo'),
(221, 'Tokelau'),
(222, 'Tonga'),
(223, 'Trinidad and Tobago'),
(224, 'Tunisia'),
(225, 'Turkey'),
(226, 'Turkmenistan'),
(227, 'Turks and Caicos Islands'),
(228, 'Tuvalu'),
(229, 'Uganda'),
(230, 'Ukraine'),
(231, 'United Arab Emirates'),
(232, 'United Kingdom'),
(233, 'United States'),
(234, 'United States Minor Outlying Islands'),
(235, 'Uruguay'),
(236, 'Uzbekistan'),
(237, 'Vanuatu'),
(238, 'Venezuela'),
(239, 'Viet Nam'),
(240, 'Virgin Islands, British'),
(241, 'Virgin Islands, U.S.'),
(242, 'Wallis And Futuna'),
(243, 'Western Sahara'),
(244, 'Yemen'),
(245, 'Zambia'),
(246, 'Zimbabwe');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `id` int(10) NOT NULL,
  `dept_name` varchar(255) NOT NULL,
  `status` enum('active','inactive') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`id`, `dept_name`, `status`) VALUES
(1, 'AA', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `equipment`
--

CREATE TABLE `equipment` (
  `id` int(10) NOT NULL,
  `equipmentid` varchar(64) NOT NULL,
  `site` varchar(64) NOT NULL,
  `department` varchar(64) NOT NULL,
  `equipment_name` varchar(64) NOT NULL,
  `equipment_type` varchar(64) NOT NULL,
  `file_equpment_info` varchar(255) NOT NULL,
  `notes` text NOT NULL,
  `create_by_user_id` int(10) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_updated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `equipment`
--

INSERT INTO `equipment` (`id`, `equipmentid`, `site`, `department`, `equipment_name`, `equipment_type`, `file_equpment_info`, `notes`, `create_by_user_id`, `date_created`, `date_updated`) VALUES
(49, 'e23233', 'Trumbull', 'AA', '2323', 'AA', '', '323232', 11, '2016-08-24 13:11:06', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `equipment_attach`
--

CREATE TABLE `equipment_attach` (
  `id` int(10) NOT NULL,
  `equipment_id` int(10) NOT NULL,
  `attach` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `equipment_type`
--

CREATE TABLE `equipment_type` (
  `id` int(10) NOT NULL,
  `equip_type_name` varchar(255) NOT NULL,
  `status` enum('active','inactive') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `equipment_type`
--

INSERT INTO `equipment_type` (`id`, `equip_type_name`, `status`) VALUES
(1, 'AA', 'active'),
(2, 'vvfd', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `left_menu`
--

CREATE TABLE `left_menu` (
  `id` int(10) NOT NULL,
  `name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `left_menu`
--

INSERT INTO `left_menu` (`id`, `name`) VALUES
(1, 'super'),
(2, 'admin'),
(3, 'only assigned'),
(4, 'can assign');

-- --------------------------------------------------------

--
-- Table structure for table `roles`
--

CREATE TABLE `roles` (
  `id` int(10) NOT NULL,
  `name` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'super'),
(2, 'admin'),
(3, 'only assigned'),
(4, 'can assign');

-- --------------------------------------------------------

--
-- Table structure for table `schedule`
--

CREATE TABLE `schedule` (
  `id` int(10) NOT NULL,
  `ticket_no` varchar(64) NOT NULL,
  `site` varchar(64) NOT NULL,
  `department` varchar(64) NOT NULL,
  `equipment_name` varchar(64) NOT NULL,
  `equipment_type` varchar(64) NOT NULL,
  `date_from` date NOT NULL,
  `time_from_min` varchar(20) NOT NULL,
  `time_from_sec` varchar(20) NOT NULL,
  `date_to` date NOT NULL,
  `time_to_min` varchar(20) NOT NULL,
  `time_to_sec` varchar(20) NOT NULL,
  `duration` varchar(64) NOT NULL,
  `notes` text NOT NULL,
  `assigned_to_users_id` int(10) NOT NULL,
  `create_by_user_id` int(10) NOT NULL,
  `date_open` date NOT NULL,
  `date_closed` date NOT NULL,
  `date_created` date NOT NULL,
  `date_updated` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `schedule`
--

INSERT INTO `schedule` (`id`, `ticket_no`, `site`, `department`, `equipment_name`, `equipment_type`, `date_from`, `time_from_min`, `time_from_sec`, `date_to`, `time_to_min`, `time_to_sec`, `duration`, `notes`, `assigned_to_users_id`, `create_by_user_id`, `date_open`, `date_closed`, `date_created`, `date_updated`) VALUES
(41, '1', 'Trumbull', 'AA', 'AAAAAA', 'AA', '2016-08-15', '22', '22', '2016-08-15', '22', '22', 'All Day', 'dgdfg dsgdfgdg sdfffsdf', 0, 12, '0000-00-00', '0000-00-00', '2016-08-14', '2016-08-14'),
(42, '13', 'Trumbull', 'AA', 'AAAAAA', 'AA', '2016-08-15', '33', '33', '2016-08-15', '33', '33', 'All Day,Repeat', '3333', 0, 12, '0000-00-00', '0000-00-00', '2016-08-14', '2016-08-14'),
(43, '2', 'Trumbull', 'XX', 'XXX', 'DD', '2016-08-15', '', '', '2016-08-15', '', '', 'All Day,Repeat', 'fhfhhh', 0, 12, '0000-00-00', '0000-00-00', '2016-08-14', '0000-00-00'),
(44, '3', 'Trumbull', 'AA', 'AAAAAA', 'AA', '2016-08-20', '434', '3434', '2016-08-20', '4343', '4343', 'All Day,Repeat', 'hhdfh   utu  yrym', 0, 12, '0000-00-00', '0000-00-00', '2016-08-19', '0000-00-00'),
(45, '31', 'Trumbull', 'AA', '2323', 'AA', '2016-08-24', '11', '11', '2016-08-24', '11', '11', 'All Day,Repeat', 'dddd', 0, 11, '0000-00-00', '0000-00-00', '2016-08-24', '2016-08-24'),
(46, '', 'Trumbull', 'AA', '2323', 'AA', '2016-08-27', '22', '22', '2016-08-28', '22', '22', 'All Day,Repeat', '2222', 0, 11, '0000-00-00', '0000-00-00', '2016-08-28', '0000-00-00'),
(47, '33', 'Trumbull', 'AA', '2323', 'AA', '2016-08-28', '34344', '3434', '2016-08-28', '4', '44', 'All Day,Repeat', '444343', 0, 11, '0000-00-00', '0000-00-00', '2016-08-28', '0000-00-00'),
(48, '50', 'Trumbull', 'AA', '2323', 'AA', '2016-08-30', '11', '11', '2016-08-30', '11', '11', 'All Day,Repeat', '111', 9, 11, '0000-00-00', '0000-00-00', '2016-08-29', '2016-08-29'),
(49, '50', 'Trumbull', 'AA', '2323', 'AA', '2016-08-30', '', '', '2016-08-30', '', '', 'All Day,Repeat', 'hghfh fdfdf dfdf', 9, 11, '2016-08-29', '0000-00-00', '2016-08-29', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `site`
--

CREATE TABLE `site` (
  `id` int(10) NOT NULL,
  `site_name` varchar(255) NOT NULL,
  `status` enum('active','inactive') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `site`
--

INSERT INTO `site` (`id`, `site_name`, `status`) VALUES
(1, 'Trumbull', 'active'),
(5, 'yyty', 'active');

-- --------------------------------------------------------

--
-- Table structure for table `ticket`
--

CREATE TABLE `ticket` (
  `id` int(10) NOT NULL,
  `ticket_no` varchar(64) NOT NULL,
  `site` varchar(64) NOT NULL,
  `department` varchar(64) NOT NULL,
  `equipment_name` varchar(64) NOT NULL,
  `equipment_type` varchar(64) NOT NULL,
  `status` enum('Up','Down','In Maintenance') NOT NULL,
  `priority` enum('Urgent','Medium','Low') NOT NULL,
  `summary` text NOT NULL,
  `ticket_status` enum('open','close') NOT NULL,
  `assigned_to_users_id` int(10) NOT NULL,
  `assigned_by_users_id` int(10) NOT NULL,
  `date_open` date NOT NULL,
  `date_closed` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `ticket`
--

INSERT INTO `ticket` (`id`, `ticket_no`, `site`, `department`, `equipment_name`, `equipment_type`, `status`, `priority`, `summary`, `ticket_status`, `assigned_to_users_id`, `assigned_by_users_id`, `date_open`, `date_closed`) VALUES
(1, '1', 'Trumbull', 'AA', '2323', 'AA', 'Up', 'Urgent', 'rrrrr', 'open', 0, 0, '2016-08-24', '0000-00-00'),
(2, '2', 'Trumbull', 'AA', '2323', 'AA', 'Up', 'Urgent', 'gfgfg', 'open', 12, 0, '2016-08-24', '0000-00-00'),
(3, '3', 'Trumbull', 'AA', '2323', 'AA', 'Up', 'Urgent', 'rryry trtert grtgert', 'open', 9, 0, '2016-08-28', '0000-00-00'),
(4, '4', 'Trumbull', 'AA', '2323', 'AA', 'Up', 'Urgent', 'sdsd', 'open', 9, 0, '2016-08-29', '0000-00-00');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `email` varchar(127) NOT NULL,
  `password` varchar(127) NOT NULL,
  `title` varchar(127) NOT NULL,
  `first_name` varchar(127) NOT NULL,
  `last_name` varchar(127) NOT NULL,
  `company` varchar(127) NOT NULL,
  `address` varchar(127) NOT NULL,
  `city` varchar(127) NOT NULL,
  `state` varchar(127) NOT NULL,
  `zip` varchar(127) NOT NULL,
  `country_id` varchar(127) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_type` enum('super','staff','client','visitor') NOT NULL,
  `left_menu` text NOT NULL,
  `roles` text NOT NULL,
  `status` enum('active','inactive') NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `title`, `first_name`, `last_name`, `company`, `address`, `city`, `state`, `zip`, `country_id`, `created_at`, `updated_at`, `user_type`, `left_menu`, `roles`, `status`) VALUES
(9, 'xx@xx.com', '123456', 'Mr.', 'Anil', 'kumar', '', '', '', '', '', '231', '2011-10-19 00:00:00', '2011-10-19 00:00:00', 'super', '', '', 'active'),
(10, 'aa@aa.com', '123456', '', 'AA', 'BB', '', '', '', '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '', '', '', 'active'),
(11, 'aa1@aa.com', '123456', '', 'AA', 'BB', '', '', '', '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'client', '', '', 'active'),
(12, 'aa11@aa.com', 'secret', '', 'AA', 'AA', '', '', '', '', '', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'client', '', '', 'active'),
(13, 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', 'xx', '243', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 'super', 'admin, can assign, only assigned', 'can assign, only assigned, super', 'active');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `equipment`
--
ALTER TABLE `equipment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `equipment_attach`
--
ALTER TABLE `equipment_attach`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `equipment_type`
--
ALTER TABLE `equipment_type`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `left_menu`
--
ALTER TABLE `left_menu`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `schedule`
--
ALTER TABLE `schedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `site`
--
ALTER TABLE `site`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ticket`
--
ALTER TABLE `ticket`
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
-- AUTO_INCREMENT for table `country`
--
ALTER TABLE `country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=247;
--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `equipment`
--
ALTER TABLE `equipment`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
--
-- AUTO_INCREMENT for table `equipment_attach`
--
ALTER TABLE `equipment_attach`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `equipment_type`
--
ALTER TABLE `equipment_type`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT for table `left_menu`
--
ALTER TABLE `left_menu`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `schedule`
--
ALTER TABLE `schedule`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;
--
-- AUTO_INCREMENT for table `site`
--
ALTER TABLE `site`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `ticket`
--
ALTER TABLE `ticket`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
