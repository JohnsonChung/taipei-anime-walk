import { defineCollection, z } from 'astro:content';

const spots = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.string(),
    name: z.string(),
    district: z.string(),
    cluster: z.enum([
      "西門商圈",
      "台北地下街",
      "光華三創",
      "公館台大",
      "台北車站周邊",
      "獨立散點"
    ]),
    type: z.array(z.string()),
    vibe: z.string(),
    stamina_cost: z.enum([
      "極低 (冷氣充沛/隨時有位)",
      "低 (動線順暢)",
      "中 (需站立穿梭)",
      "高 (長程跋涉/人潮擠壓)"
    ]),
    backpack_friendly: z.enum([
      "友善 (通道寬敞)",
      "適中",
      "極度狹窄 (需前背/卸包)"
    ]),
    coordinates: z.tuple([z.number(), z.number()]), // [lng, lat]
    google_maps_url: z.string().url().optional(),
    status: z.enum(["active", "archive"]).default("active"),
    closed_year: z.number().optional(),
    contributor: z.string().default("@curator"),
    updated_at: z.string().optional()
  })
});

const walks = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.string(),
    title: z.string(),
    subtitle: z.string(),
    target_cluster: z.string(),
    estimated_duration: z.string(),
    total_stamina_cost: z.number().min(1).max(5),
    spot_sequence: z.array(z.string()),
    loot_sorting_spot: z.string(),
    rest_anchor: z.string(),
    cover_image: z.string().optional(),
    featured: z.boolean().default(false)
  })
});

export const collections = { spots, walks };
