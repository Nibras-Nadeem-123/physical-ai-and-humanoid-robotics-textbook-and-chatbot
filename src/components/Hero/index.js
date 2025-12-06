import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

export function Hero({ children }) {
  return <div className={styles.hero}>{children}</div>;
}

export function HeroBanner({ children }) {
  return <div className={styles.heroBanner}>{children}</div>;
}

export function HeroTitle({ children }) {
  return <h1 className={styles.heroTitle}>{children}</h1>;
}

export function HeroSubtitle({ children }) {
  return <p className={styles.heroSubtitle}>{children}</p>;
}

export function HeroButtons({ children }) {
  return <div className={styles.heroButtons}>{children}</div>;
}
